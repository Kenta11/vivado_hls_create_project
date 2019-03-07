#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import xml.etree.ElementTree as ET

import code_generator
from message import *
import util

# parse_args()
# - parse arguments
# - return values
#     - project: project name that is expected *str* type.
#     - board: board name that is expected *str* type. This name can be listed with list_devices()
#     - solution: solutin name that is expected *str* type.
#     - clock: clock that is expected *str* type, like "100MHz", "10.0ns", etc.
#     - l: flag of listing that is expected *bool* type.
#     - C: flag of C++ code generation that is expected *bool* type.
def parse_args():
    parser = argparse.ArgumentParser(description="generate Makefile and tcl scripts")
    parser.add_argument("-l", action="store_true", help="listing devices")
    parser.add_argument("-p", "--project", help="project name")
    parser.add_argument("-b", "--board", help="board name")
    parser.add_argument("-s", "--solution", help="solution name")
    parser.add_argument("-c", "--clock", help="frequency or clock period")
    parser.add_argument("-cpp", action="store_true", help="generate C++ code")
    parser.add_argument("-compiler_arg", help="argument for compiler")
    parser.add_argument("-linker_arg", help="argument for linker")

    args = parser.parse_args()

    project = args.project
    board = args.board

    solution = args.solution
    if solution is None:
        solution = board

    clock = args.clock

    listing = args.l

    cpp = args.cpp
    if cpp is None:
        cpp = False

    return {
        "project": project,
        "solution": solution,
        "board": board,
        "clock": clock,
        "listing": listing,
        "cpp": cpp,
        "compiler_arg": args.compiler_arg,
        "linker_arg": args.linker_arg
    }

# list_devices()
# - list device names
# - names are loaded from /path/to/Vivado/20xx.x/common/config/VivadoHls_boards.xml
def list_devices():
    tree = ET.parse(util.path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    print("Board" + (" " * 15) + "Part")
    print("----------------------------")
    for platform in root:
        for board in platform:
            print(board.attrib["name"], end="")
            print(" " * (20 - len(board.attrib["name"])), end="")
            print(board.attrib["part"])

# search_device()
# - search device name from VivadoHls_boards.xml
# - names are loaded from /path/to/Vivado/20xx.x/common/config/VivadoHls_boards.xml
def search_device(board_name):
    tree = ET.parse(util.path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    for platform in root:
        for board in platform:
            if board.attrib["name"] == board_name:
                print_INFO("Found part")
                return board.attrib["device"] + board.attrib["package"] + board.attrib["speedgrade"]

    print_ERROR("Not found part")
    return None

# generate_code()
# - generate Makefile and tcl scripts
def generate_code(args):
    code_generator.generate_makefile(args["project"], args["solution"])
    code_generator.generate_dirs()
    code_generator.generate_tcl(args["part"], args["clock"], args["compiler_arg"], args["linker_arg"])
    if args["cpp"]:
        code_generator.generate_cpp_code(args["project"])

#########################
##### main function #####
#########################
def vivado_hls_create_project():
    args = parse_args()

    # listing device name
    if args["listing"] == True:
        list_devices()
    # generate source code
    elif args["listing"] == False:
        if args["project"] is None:
            print_ERROR("set project name")
            exit(1)

        args["part"] = search_device(args["board"])
        if args["part"] is None:
            print_ERROR("set board name")
            exit(1)

        if args["solution"] is None:
            args["solution"] = board

        if args["clock"] is None:
            args["clock"] = "100MHz"

        generate_code(args)
    # no argument
    else:
        print_ERROR("Invalid arguments")

if __name__ == '__main__':
    vivado_hls_create_project()
