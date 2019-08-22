#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import xml.etree.ElementTree as ET

from logzero import logger
from pathlib import Path

def getPathToVivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return Path(json.load(f)["path_to_vivado"])

def getBoardInfo():
    board_info = {}
    path_to_board_files = getPathToVivado() / "data/boards/board_files"
    dirnames = [\
        path_to_board_files / f for f in os.listdir(path_to_board_files)\
        if os.path.isdir(os.path.join(path_to_board_files, f))\
    ]

    for d in dirnames:
        if os.path.isfile(d / "board.xml"):
            board_info[os.path.basename(d)] = ET.parse(Path(d) / "board.xml").getroot()
        else:
            for sub_d in sorted([d / sub_d for sub_d in os.listdir(d)]):
                if os.path.isfile(sub_d / "board.xml"):
                    board_info[os.path.basename(d)] = ET.parse(sub_d / "board.xml").getroot()
                    break
    return board_info

def listDevices():
    board_info:dict = getBoardInfo()

    print("Board", (" " * 13), "Part")
    print("-" * 50)
    for key in board_info:
        comp = board_info[key].findall("components/component[@type='fpga']")
        if comp != []:
            print(
                key, " " * (18 - len(key)),
                comp[0].attrib["part_name"]
            )

def searchDevice(board_name: str):
    board_info:dict = getBoardInfo()
    if board_name not in board_info.keys():
        logger.error("{}'s part not found".format(board_name))
        return (None, None)
    
    component = board_info[board_name].findall(\
        "components/component[@type='fpga']"\
    )[0]
    part_name = component.attrib["part_name"]

    clock = 0
    interface = component.findall(\
        "interfaces/interface[@name='sys_clock']"\
    )
    if interface != []:
        clock = interface[0].findall(\
            "parameters/parameter[@name='frequency']"\
        )[0].attrib["value"]
    else:
        clock = component.findall(\
            "interfaces/interface[@name='sys_diff_clock']"\
        )[0].findall(\
            "parameters/parameter[@name='frequency']"\
        )[0].attrib["value"]

    return (part_name, str(int(clock) // 10 ** 6)+"MHz")
