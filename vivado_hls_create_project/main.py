#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

from logzero import logger

from . import generator
from . import argparser
from . import deviceinfo

def main():
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
            logger.error("Key error: key={} config={}".format(config["arg"][0], data))
    else:
        logger.error("Invalid arguments")

if __name__ == '__main__':
    main()
