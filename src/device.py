#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import xml.etree.ElementTree as ET

from message import print_INFO, print_WARNING, print_ERROR

# path_to_vivado()
# - load Vivado path from "~/..vivado_hls_create_project"
def path_to_vivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return json.load(f)["path_to_vivado"]

# list_devices()
# - list device names
# - names are loaded from /path/to/Vivado/20xx.x/common/config/VivadoHls_boards.xml
def list_devices():
    tree = ET.parse(path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    print("Board", (" " * 13), "Part")
    print("-" * 50)
    for platform in root:
        for board in platform:
            print(board.attrib["name"], end="")
            print(" " * (20 - len(board.attrib["name"])), end="")
            print(board.attrib["part"])

# search_device()
# - search device name from VivadoHls_boards.xml
# - names are loaded from /path/to/Vivado/20xx.x/common/config/VivadoHls_boards.xml
def search_device(board_name: str):
    tree = ET.parse(path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    for platform in root:
        for board in platform:
            if board.attrib["name"] == board_name:
                part_name = board.attrib["device"] + board.attrib["package"] + board.attrib["speedgrade"]
                print_INFO("Part of {} found -> {}".format(board_name, part_name))
                return part_name

    print_ERROR("Part not found")
    return None

