#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import pathlib

import jinja2

from message import *

base_path = os.path.dirname(os.path.dirname(__file__))

# generate_makefile()
# - generate Makefile from template/Makefile
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

# generate_dirs()
# - generate the following directories
#     - include/
#     - src/
#     - test/include/
#     - test/src/
#     - script
def generate_dirs():
    os.makedirs("include")
    os.makedirs("src")
    os.makedirs("test/include")
    os.makedirs("test/src")
    os.makedirs("script")

    print_INFO("Generate directories")

# generate_tcl()
# - generate tcl scripts from template/tcl/*
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
