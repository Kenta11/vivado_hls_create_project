#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# path_to_vivado()
# - load Vivado path from "~/..vivado_hls_create_project"
def path_to_vivado():
    with open(os.path.expanduser("~/.vivado_hls_create_project")) as f:
        return json.load(f)["path_to_vivado"]
