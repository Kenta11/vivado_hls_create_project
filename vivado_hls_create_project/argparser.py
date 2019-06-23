#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from logzero import logger
from pathlib import Path

def parseArgs(argv):
    config = {\
        "command": None,\
        "project": None,\
        "board": None,\
        "help": False,\
        "solution": None,\
        "clock": None,\
        "template": False,\
        "compiler_argument": None,\
        "linker_argument": None\
    }

    # parse arguments
    if len(argv) > 0:
        if argv[0] in ["list", "create"]:
            config["command"] = argv[0]
        elif argv[0] in ["-h", "--help"]:
            config["help"] = True

    index = 1
    try:
        while index < len(argv):
            if argv[index] in ["-h", "--help"]:
                if config["help"] is False:
                    config["help"]              = True
                    index += 1
                else:
                    raise Exception
            elif index+1 == len(argv):
                config["project"]               = argv[index]
                index += 1
            elif argv[index] in ["-b", "--board"]:
                if config["board"] is None:
                    config["board"]             = argv[index+1]
                    index += 2
                else:
                    raise Exception
            elif argv[index] in ["-s", "--solution"]:
                if config["solution"] is None:
                    config["solution"]          = argv[index+1]
                    index += 2
                else:
                    raise Exception
            elif argv[index] in ["-c", "--clock"]:
                if config["clock"] is None:
                    config["clock"]             = argv[index+1]
                    index += 2
                else:
                    raise Exception
            elif argv[index] in ["--template"]:
                if config["template"] is False:
                    config["template"]          = True
                    index += 1
                else:
                    raise Exception
            elif argv[index] in ["--compiler_argument"]:
                if config["compiler_argument"] is None:
                    config["compiler_argument"] = argv[index+1]
                    index += 2
                else:
                    raise Exception
            elif argv[index] in ["--linker_argument"]:
                if config["linker_argument"] is None:
                    config["linker_argument"]   = argv[index+1]
                    index += 2
                else:
                    raise Exception
            else:
                raise Exception
    except IndexError:
        logger.error("Invalid format of arguments")
        exit(1)
    except Exception:
        logger.error("Arguments are invalid")
        exit(1)

    # check arguments
    if config["command"] is None or config["help"] is True:
        printUsage(config["command"])
        exit(1)
    elif config["command"] == "create":
        if config["project"] is None or config["board"] is None:
            logger.error("<project_name> and <board_name> are required")
            exit(1)
    if config["solution"] is None:
        config["solution"] = config["project"]
    if config["clock"] is None:
        config["clock"] = "100MHz"

    return config

def printUsage(command):
    with open(Path(os.path.dirname(__file__)) / "usage" / str(command), "r") as f:
        print(f.read())
