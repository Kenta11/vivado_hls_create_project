#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def get_config():
    args = parse_args()

    config = { "command": args.command }
    if args.command == "create":
        # project
        config["project"] = args.project_name
        # solution
        if args.solution is None:
            config["solution"] = args.board
        else:
            config["solution"] = args.solution
        # board
        config["board"] = args.board
        # clock
        config["clock"] = args.clock
        # template
        config["template"] = args.template
        # compiler_arg
        config["compiler_arg"] = args.compiler_arg
        # linker_arg
        config["linker_arg"] = args.linker_arg

    return config

def parse_args():
    parser = argparse.ArgumentParser(\
        description="Makefile and tcl scripts generator for Vivado HLS"\
    )

    subparser = parser.add_subparsers()

    # list command
    parser_list = subparser.add_parser("list", help = "List usable boards")
    ## command name
    parser_list.set_defaults(command = "list")

    # create command
    parser_create = subparser.add_parser("create", help="Create Makefile and tcl scripts")
    ## command name
    parser_create.set_defaults(command = "create")
    ## positional arguments
    parser_create.add_argument("project_name")
    ## optional arguments
    parser_create.add_argument(\
        "-s", "--solution",\
        help = "Solution name"\
    )
    parser_create.add_argument(\
        "-c", "--clock",\
        default = "100MHz",\
        help = "Clock frequency of module"\
    )
    parser_create.add_argument(\
        "--template",\
        action="store_true",\
        help="Option for C++ template source code generation"\
    )
    parser_create.add_argument("--compiler_arg", help = "Arguments for compiler")
    parser_create.add_argument("--linker_arg",   help = "Arguments for linker")
    parser_create.add_argument(\
        "-b", "--board",\
        required = True,\
        help = "Board name"\
    )

    return parser.parse_args()
