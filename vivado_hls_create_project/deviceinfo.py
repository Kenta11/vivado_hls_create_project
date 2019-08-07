#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import xml.etree.ElementTree as ET

from logzero import logger
from pathlib import Path

def getPathToVivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return json.load(f)["path_to_vivado"]

def getBoardInfo():
    roots = {}
    path_to_board_files = Path(getPathToVivado()) / "data/boards/board_files"
    dirnames = [\
        path_to_board_files / f for f in os.listdir(path_to_board_files)\
        if os.path.isdir(os.path.join(path_to_board_files, f))\
    ]

    for d in dirnames:
        if os.path.isfile(d / "board.xml"):
            roots[os.path.basename(d)] = ET.parse(Path(d) / "board.xml").getroot()
        else:
            for sub_d in sorted([d / sub_d for sub_d in os.listdir(d)]):
                if os.path.isfile(sub_d / "board.xml"):
                    roots[os.path.basename(d)] =\
                    ET.parse(sub_d / "board.xml").getroot()
                    break
    return roots

def listDevices():
    roots = getBoardInfo()

    print("Board", (" " * 13), "Part")
    print("-" * 50)
    for root_key in roots:
        for component in roots[root_key].iter("component"):
            if component.attrib["type"] == "fpga":
                print(
                    root_key, " " * (18 - len(root_key)),
                    component.attrib["part_name"]
                )
                break

def searchDevice(board_name: str):
    roots = getBoardInfo()

    for root_key in roots:
        for component in roots[root_key].iter("component"):
            if component.attrib["type"] == "fpga" and root_key == board_name:
                part_name = component.attrib["part_name"]
                logger.info("{}'s part found -> {}".format(board_name, part_name))
                return part_name

    logger.error("{}'s part not found".format(board_name))
    return None
