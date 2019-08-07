#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2
import os
import shutil

from logzero import logger
from pathlib import Path

from . import deviceinfo

def createProject(config):
    generateDirectories(config["project"])
    generateCode(config)

def generateDirectories(project_name:str):
    generateDirectory(project_name)
    generateDirectory(project_name+"/include")
    generateDirectory(project_name+"/src")
    generateDirectory(project_name+"/test/include")
    generateDirectory(project_name+"/test/src")
    generateDirectory(project_name+"/script")

def generateCode(config):
    os.chdir(config["project"])

    generateMakefile(config["project"], config["solution"])
    generateTcl(config["board"], config["clock"], config["compiler_argument"], config["linker_argument"])
    generateDirectives()
    generateGitignore(config["project"])
    generateSourceCode(config["project"])

    os.chdir("../")

def generateDirectory(name:str):
    if os.path.isdir(name):
        logger.warning("{} exists! Skipping...".format(name))
    elif os.path.isfile(name):
        logger.error("{} is a file!".format(name))
        exit(1)
    else:
        logger.info("generate {}".format(name))
        os.makedirs(name, exist_ok = True)

def generateMakefile(project:str, solution:str):
    logger.info("generate Makefile")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
         str(Path(os.path.dirname(__file__)) / "template")\
    ))
    template = env.get_template("Makefile")
    data = {
        "TARGET": project,
        "SOLUTION": solution
    }
    rendered = template.render(data)
    with open("Makefile", "w") as f:
        f.write(str(rendered))

def generateTcl(board:str, clock:str, compiler_arg, linker_arg):
    logger.info("generate tcl scripts")

    ##### cosim.tcl, export.tcl #####
    for name in ["cosim.tcl", "export.tcl"]:
        shutil.copy(\
            str(Path(os.path.dirname(__file__)) / "template/tcl/{}".format(name)),\
            "script/{}".format(name)\
        )

    ##### init.tcl #####
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
        str(Path(os.path.dirname(__file__)) / "template/tcl")\
    ))
    template = env.get_template("init.tcl")
    COMPILER_ARG = ""
    if compiler_arg is not None:
        COMPILER_ARG = compiler_arg
    data = {
        "COMPILER_ARG": COMPILER_ARG
    }
    rendered = template.render(data)
    with open("script/init.tcl", "w") as f:
        f.write(str(rendered))

    ##### csim.tcl #####
    template = env.get_template("csim.tcl")
    LINKER_ARG = ""
    if linker_arg is not None:
        LINKER_ARG = "-ldflags \"{}\"".format(linker_arg)
    data = {
        "LINKER_ARG": LINKER_ARG
    }
    rendered = template.render(data)
    with open("script/csim.tcl", "w") as f:
        f.write(str(rendered))

    ##### csynth.tcl #####
    template = env.get_template("csynth.tcl")
    data = {
        "PART": "{" + deviceinfo.searchDevice(board) + "}",
        "CLOCK": clock
    }
    rendered = template.render(data)
    with open("script/csynth.tcl", "w") as f:
        f.write(str(rendered))

def generateDirectives():
    logger.info("generate directives.tcl")

    Path("directives.tcl").touch()

def generateGitignore(project:str):
    logger.info("generate .gitignore")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
        str(Path(os.path.dirname(__file__)) / "template")\
    ))
    template = env.get_template("gitignore")
    data = {
        "TARGET": project
    }
    rendered = template.render(data)
    with open(".gitignore", "w") as f:
        f.write(str(rendered))

def generateSourceCode(target:str):
    logger.info("generate source code")

    data = {
        "target": target,
        "TARGET": target.upper()
    }
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(\
        str(Path(os.path.dirname(__file__)) / "template/c++")\
    ))

    for src, dst in zip(\
        ["header.hpp", "code.cpp", "test-header.hpp", "test-code.cpp"],\
        ["include/{}.hpp", "src/{}.cpp", "test/include/test_{}.hpp", "test/src/test_{}.cpp"]\
    ):
        template = env.get_template(src)
        rendered = template.render(data)
        with open(dst.format(target), "w") as f:
            f.write(str(rendered))
