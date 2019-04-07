#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import pathlib

import jinja2

import device
from message import print_INFO, print_WARNING, print_ERROR

base_path = os.path.dirname(os.path.dirname(__file__))

def create_project(config):
    generate_directories(config["project"])
    generate_code(config)

# generate_directory
# - generate one directory
#     - if there is a directory named <name>, skip
#     - if there is a file named <name>, discontinue
def generate_directory(name: str):
    print_INFO("Generating directory " + name)

    if os.path.isdir(name):
        print_WARNING(name + " exists! Skipping...")
    elif os.path.isfile(name):
        print_ERROR(name + " is a file!")
        exit(1)
    else:
        os.makedirs(name, exist_ok = True)

def generate_Makefile(project, solution):
    print_INFO("Generating Makefile")

    # generate Makefile
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
        base_path + "/template")\
    )
    template = env.get_template("Makefile")
    data = {
        "TARGET": project,
        "SOLUTION": solution
    }
    rendered = template.render(data)
    # save Makefile
    with open("Makefile", "w") as f:
        f.write(str(rendered))

def generate_tcl(board, clock, compiler_arg, linker_arg):
    print_INFO("Generating tcl scripts")

    ##### cosim.tcl, export.tcl #####
    # generate cosim.tcl, export.tcl
    shutil.copy(base_path + "/template/tcl/cosim.tcl",  "script/cosim.tcl")
    shutil.copy(base_path + "/template/tcl/export.tcl", "script/export.tcl")

    ##### init.tcl #####
    # generate init.tcl
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/tcl"))
    template = env.get_template("init.tcl")
    COMPILER_ARG = compiler_arg if compiler_arg is not None else ""
    data = {
        "COMPILER_ARG": COMPILER_ARG
    }
    rendered = template.render(data)
    # save init.tcl
    with open("script/init.tcl", "w") as f:
        f.write(str(rendered))

    ##### csim.tcl #####
    # generate csim.tcl
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/tcl"))
    template = env.get_template("csim.tcl")
    LINKER_ARG = "\"-ldflags{}\"".format(linker_arg) if linker_arg is not None else ""
    data = {
        "LINKER_ARG": LINKER_ARG
    }
    rendered = template.render(data)
    # save csim.tcl
    with open("script/csim.tcl", "w") as f:
        f.write(str(rendered))

    ##### csynth.tcl #####
    # generate csynth.tcl
    template = env.get_template("csynth.tcl")
    data = {
        "PART": "{" + device.search_device(board) + "}",
        "CLOCK": clock
    }
    rendered = template.render(data)

    # save csynth.tcl
    with open("script/csynth.tcl", "w") as f:
        f.write(str(rendered))

def generate_directives():
    print_INFO("Generating directives.tcl")
    # generate directives.tcl
    pathlib.Path("directives.tcl").touch()

def generate_gitignore(project: str):
    print_INFO("Generating .gitignore")

    # generate .gitignore
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
        base_path + "/template")\
    )
    template = env.get_template(".gitignore")
    data = {
        "TARGET": project
    }
    rendered = template.render(data)
    # save .gitignore
    with open(".gitignore", "w") as f:
        f.write(str(rendered))

def generate_source_code(target: str):
    print_INFO("Generating template C++ source code")

    data = {
        "target": target,
        "TARGET": target.upper()
    }

    # generate hpp
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/c++/"))
    template = env.get_template("header.hpp")
    rendered = template.render(data)
    with open("include/" + target + ".hpp", "w") as f:
        f.write(str(rendered))

    # generate cpp
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/c++/"))
    template = env.get_template("code.cpp")
    rendered = template.render(data)
    with open("src/" + target + ".cpp", "w") as f:
        f.write(str(rendered))

    # generate test hpp
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/c++/"))
    template = env.get_template("test-header.hpp")
    rendered = template.render(data)
    with open("test/include/test_" + target + ".hpp", "w") as f:
        f.write(str(rendered))

    # generate test cpp
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_path + "/template/c++/"))
    template = env.get_template("test-code.cpp")
    rendered = template.render(data)
    with open("test/src/test_" + target + ".cpp", "w") as f:
        f.write(str(rendered))

# generate_directories()
# - generate the following directories
# <project_name>
# <project_name>/include/
# <project_name>/src/
# <project_name>/test/include/
# <project_name>/test/src/
# <project_name>/script/
def generate_directories(project_name: str):
    generate_directory(project_name)
    generate_directory(project_name+"/include")
    generate_directory(project_name+"/src")
    generate_directory(project_name+"/test/include")
    generate_directory(project_name+"/test/src")
    generate_directory(project_name+"/script")

# generate_code()
# - basic
#     - generate the following source code
#     - Makefile
#     - tcl/{init.tcl, csim.tcl csynth.tcl, cosim.tcl, export.tcl}
#     - directives.tcl
# - option
#     - include/<project_name>.hpp
#     - src/<project_name>.hpp
#     - test/include/test_<project_name>.hpp
#     - test/src/test_<project_name>.hpp
def generate_code(config):
    os.chdir(config["project"])

    # basical source code
    generate_Makefile(config["project"], config["solution"])
    generate_tcl(config["board"], config["clock"], config["compiler_arg"], config["linker_arg"])
    generate_directives()
    generate_gitignore(config["project"])

    # optional source code
    if config["template"]:
        generate_source_code(config["project"])

    os.chdir("../")
