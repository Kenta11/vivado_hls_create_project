#!/usr/bin/env zsh
#! -*- coding: utf-8 -*-

PATH_TO_VIVADO_HLS_CREATE_PROJECT=$(cd $(dirname $0); pwd)/src/vivado_hls_create_project.py
alias vivado_hls_create_project="python3 $PATH_TO_VIVADO_HLS_CREATE_PROJECT"
