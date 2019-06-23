#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from logzero import logger

from . import generator
from . import argparser
from . import deviceinfo

def main():
    config = argparser.parseArgs(sys.argv[1:])
    
    if config["command"] == "create":
        generator.createProject(config)
    elif config["command"] == "list":
        deviceinfo.listDevices()
    else:
        logger.error("Invalid arguments")

if __name__ == '__main__':
    main()
