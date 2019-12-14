#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys

from logzero import logger

from vivado_hls_create_project import generator
from vivado_hls_create_project import argparser
from vivado_hls_create_project import deviceinfo

def main()->None:
    config = argparser.parseArgs(sys.argv[1:])
    path_to_config = os.path.expanduser("~/.vivado_hls_create_project")

    if config["command"] == "create":
        generator.createProject(config)
    elif config["command"] == "list":
        deviceinfo.listDevices()
    elif config["command"] == "set-config":
        try:
            data = json.load(open(path_to_config))
        except FileNotFoundError:
            data = {}
        except json.decoder.JSONDecodeError:
            logger.error("Invalid JSON format: ~/.vivado_hls_create_project")
            exit(1)

        data[config["arg"][0]] = config["arg"][1]

        with open(path_to_config, "w") as f:
            json.dump(data, f)

    elif config["command"] == "get-config":
        try:
            data = json.load(open(path_to_config))
        except FileNotFoundError:
            logger.error("~/.vivado_hls_create_project not found")
            exit(1)
        except json.decoder.JSONDecodeError:
            logger.error("Invalid JSON format: ~/.vivado_hls_create_project")
            exit(1)

        try:
            print(data[config["arg"][0]])
        except KeyError:
            logger.error("Key error: key={}".format(config["arg"][0]))
    else:
        logger.error("Invalid arguments")
