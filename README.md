# vivado_hls_create_project

[日本語版](README-jp.md)

## What is vivado_hls_create_project ?

Generate Makefile and tcl scripts for creating Vivado HLS project.

## Basic Usage

### Generate Makefile and tcl scripts

Type `project name` and `board name`

```
$ vivado_hls_create_project -p `project name` -b `board name`
```

### Help

```
$ vivado_hls_create_project --help
usage: vivado_hls_create_project.py [-h] [-p PROJECT] [-b BOARD] [-s SOLUTION] [-c CLOCK] [-l]

generate Makefile and tcl scripts

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT, --project PROJECT
                        project name
  -b BOARD, --board BOARD
                        board name
  -s SOLUTION, --solution SOLUTION
                        solution name
  -c CLOCK, --clock CLOCK
                        frequency or clock period
  -l                    listing devices
```

## LICENSE

MIT License

## CONTACT

Author: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
