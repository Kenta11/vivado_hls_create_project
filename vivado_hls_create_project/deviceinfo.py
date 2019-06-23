#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import xml.etree.ElementTree as ET

from logzero import logger
from pathlib import Path

def path_to_vivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return json.load(f)["path_to_vivado"]

def listDevices():
    tree = ET.parse(str(Path(path_to_vivado()) / "common/config/VivadoHls_boards.xml"))
    root = tree.getroot()

    print("Board", (" " * 13), "Part")
    print("-" * 50)
    for platform in root:
        for board in platform:
            print(board.attrib["name"], end="")
            print(" " * (20 - len(board.attrib["name"])), end="")
            print(board.attrib["part"])

def searchDevice(board_name: str):
    tree = ET.parse(str(Path(path_to_vivado()) / "common/config/VivadoHls_boards.xml"))
    root = tree.getroot()

    for platform in root:
        for board in platform:
            if board.attrib["name"] == board_name:
                part_name = board.attrib["device"] + board.attrib["package"] + board.attrib["speedgrade"]
                logger.info("Part of {} found -> {}".format(board_name, part_name))
                return part_name

    logger.error("Part not found")
    return None
