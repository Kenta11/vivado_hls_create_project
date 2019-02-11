# vim: fileencoding=utf-8

import argparse
import os
import shutil
import json
import pathlib
import xml.etree.ElementTree as ET

import jinja2

base_path = os.path.dirname(os.path.dirname(__file__))

def print_INFO(message):
    print("INFO: ", message)

def print_WARNING(message):
    print("INFO:", message)

def print_ERROR(message):
    print("ERROR:", message)

def parse_args():
    parser = argparse.ArgumentParser(description="generate Makefile and tcl scripts")
    parser.add_argument("-p", "--project", help="project name")
    parser.add_argument("-b", "--board", help="board name")
    parser.add_argument("-s", "--solution", help="solution name")
    parser.add_argument("-c", "--clock", help="frequency or clock period")
    parser.add_argument("-l", action="store_true", help="listing devices")

    args = parser.parse_args()

    project = args.project
    board = args.board

    solution = args.solution
    if solution is None:
        solution = board

    clock = args.clock
    if clock is None:
        clock = "100MHz"

    listing = args.l

    return (project, solution, board, clock, listing)

def path_to_vivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return json.load(f)["path_to_vivado"]

def search_device(board_name):
    tree = ET.parse(path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    for platform in root:
        for board in platform:
            if board.attrib["name"] == board_name:
                print_INFO("Found part")
                return board.attrib["device"] + board.attrib["package"] + board.attrib["speedgrade"]

    print_ERROR("Not found part")
    return None

def list_devices():
    tree = ET.parse(path_to_vivado() + "/common/config/VivadoHls_boards.xml")
    root = tree.getroot()

    print("Board" + (" " * 15) + "Part")
    print("----------------------------")
    for platform in root:
        for board in platform:
            print(board.attrib["name"], end="")
            print(" " * (20 - len(board.attrib["name"])), end="")
            print(board.attrib["part"])

def generate_makefile(project, solution):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template"))
    template = env.get_template("Makefile")
    data = {
        "TARGET": project,
        "SOLUTION": solution
    }
    
    rendered = template.render(data)

    with open("Makefile", "w") as f:
        f.write(str(rendered))

    print_INFO("Generate Makefile")

def generate_dirs():
    os.makedirs("include")
    os.makedirs("src")
    os.makedirs("test/include")
    os.makedirs("test/src")
    os.makedirs("script")

    print_INFO("Generate directories")

def generate_tcl(part, clock):
    shutil.copy(base_path + "/template/tcl/csim.tcl",   "script/csim.tcl")
    shutil.copy(base_path + "/template/tcl/export.tcl", "script/export.tcl")
    shutil.copy(base_path + "/template/tcl/cosim.tcl",  "script/cosim.tcl")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/tcl"))
    template = env.get_template("csynth.tcl")
    data = {
        "PART": "{" + part + "}",
        "CLOCK": clock
    }

    rendered = template.render(data)

    with open("script/csynth.tcl", "w") as f:
        f.write(str(rendered))

    pathlib.Path("directives.tcl").touch()

    print_INFO("Generate tcl scripts")

def vivado_hls_create_project():
    project, solution, board, clock, listing = parse_args()
    if listing:
        list_devices()
    else:
        if project is None:
            print_ERROR("set project name")
            exit(1)
        if solution is None:
            solution = board
        part = search_device(board)
        if part is None:
            exit(1)

        generate_makefile(project, solution)
        generate_dirs()
        generate_tcl(part, clock)

if __name__ == '__main__':
    vivado_hls_create_project()
