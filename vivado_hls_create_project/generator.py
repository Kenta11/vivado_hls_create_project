#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2
import os
import shutil

from logzero import logger
from pathlib import Path

from vivado_hls_create_project import deviceinfo

def createProject(config)->None:
    if os.path.exists(config["project"]):
        logger.error("Directory {} already exists".format(config["project"]))
        exit(1)
    for d in ["include", "src", "test/include", "test/src", "script"]:
        os.makedirs(Path(config["project"])/d)

    os.chdir(config["project"])

    generateMakefile(config["project"], config["solution"])
    generateTcl(
        config["board"],
        config["clock"],
        config["compiler_argument"],
        config["linker_argument"]
    )
    generateDirectives()
    generateGitignore(config["project"])
    generateSourceCode(config["project"])

    os.chdir("../")

def generateMakefile(project:str, solution:str)->None:
    logger.info("generate Makefile")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
         str(Path(os.path.dirname(__file__))/"template")
    ))
    template = env.get_template("Makefile")
    data = {
        "TARGET": project,
        "SOLUTION": solution
    }
    with open("Makefile", "w") as f:
        f.write(str(template.render(data)))

def generateTcl(board:str, clock:str, compiler_arg, linker_arg)->None:
    logger.info("generate tcl scripts")

    ##### cosim.tcl, export.tcl #####
    for name in ["cosim.tcl", "export.tcl"]:
        shutil.copy(
            str(Path(os.path.dirname(__file__))/"template/tcl"/name),
            "script/"+name
        )

    ##### init.tcl #####
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
        str(Path(os.path.dirname(__file__))/"template/tcl")
    ))
    template = env.get_template("init.tcl")
    COMPILER_ARG = ""
    if compiler_arg is not None:
        COMPILER_ARG = compiler_arg
    data = {
        "COMPILER_ARG": COMPILER_ARG
    }
    with open("script/init.tcl", "w") as f:
        f.write(str(template.render(data)))

    ##### csim.tcl #####
    template = env.get_template("csim.tcl")
    LINKER_ARG = ""
    if linker_arg is not None:
        LINKER_ARG = "-ldflags \"{}\"".format(linker_arg)
    data = {
        "LINKER_ARG": LINKER_ARG
    }
    with open("script/csim.tcl", "w") as f:
        f.write(str(template.render(data)))

    ##### csynth.tcl #####
    template = env.get_template("csynth.tcl")
    part, base_clock = deviceinfo.searchDevice(board)
    data = {
        "PART": "{" + part + "}",
        "CLOCK": clock if clock is not None else base_clock
    }
    with open("script/csynth.tcl", "w") as f:
        f.write(str(template.render(data)))

def generateDirectives()->None:
    logger.info("generate directives.tcl")

    Path("directives.tcl").touch()

def generateGitignore(project:str)->None:
    logger.info("generate .gitignore")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
        str(Path(os.path.dirname(__file__))/"template")
    ))
    template = env.get_template("gitignore")
    data = {
        "TARGET": project
    }
    with open(".gitignore", "w") as f:
        f.write(str(template.render(data)))

def generateSourceCode(target:str)->None:
    logger.info("generate source code")

    data = {
        "target": target,
        "TARGET": target.upper()
    }
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
        str(Path(os.path.dirname(__file__))/"template/c++")
    ))

    srcs = ["header.hpp", "code.cpp", "test-code.cpp"]
    dsts = ["include/{}.hpp", "src/{}.cpp", "test/src/test_{}.cpp"]
    for src, dst in zip(srcs, dsts):
        template = env.get_template(src)
        with open(dst.format(target), "w") as f:
            f.write(str(template.render(data)))
