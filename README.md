# vivado_hls_create_project

日本語バージョン: [vivado_hls_create_project](README-jp.md)

## Overview

A tool to automatically generate Makefile and tcl scripts for creating Vivado HLS projects.

## Requirements

- Python3
- GNU make

## Install vivado_hls_create_project

```
$ sudo pip install git+https://github.com/Kenta11/vivado_hls_create_project
$ vivado_hls_create_project set-config path_to_vivado /path/to/Xilinx/Vivado/20xx.x
# set absolute path to Vivado on /path/to/Xilinx/Vivado/20xx.x
```

## Basic Usage

Functions can be selected by subcommands, like *git*.

```
Usage: vivado_hls_create_project [-h|--help] <command> [<args>]

Makefile and tcl scripts generator for Vivado HLS

<command>:
    list         list usable boards
    create       create Makefile and tcl scripts
    set-config   set parameter into ~/.vivado_hls_create_project
    get-config   get parameter from ~/.vivado_hls_create_project

optional arguments:
  -h, --help     show this help message and exit
```

Subcommands `list`,`create`,`set-config` and `get-config` are usable.

### vivado_hls_create_project create

Enter project name (sample) and a board name (Xilinx_ZedBoard) as follows.

```
$ vivado_hls_create_project create -b Xilinx_ZedBoard sample 
```

sample directory is generated and Makefile and tcl scripts are generated under the directory.

```
$ tree sample
sample
├ ─ ─  Makefile
├ ─ ─  directives.tcl
├ ─ ─  include
│    └ ─ ─  sample.hpp
├ ─ ─  script
│    ├ ─ ─  cosim.tcl
│    ├ ─ ─  csim.tcl
│    ├ ─ ─  csynth.tcl
│    ├ ─ ─  export.tcl
│    └ ─ ─  init.tcl
├ ─ ─  src
│    └ ─ ─  sample.cpp
└ ─ ─  test
    ├ ─ ─  include
    │    └ ─ ─  test_sample.hpp
    └ ─ ─  src
        └ ─ ─  test_sample.cpp

6 directories, 11 files
```

See `create -h` for more options.

### vivado_hls_create_project list

`list` shows boards name that can be specified with `create` subcommand.

```
$ vivado_hls_create_project list
Board               Part
--------------------------------------------------
basys3              xc7a35tcpg236-1
cmod-s7-25          xc7s25csga225-1
nexys4              xc7a100tcsg324-1
sword               xc7k325tffg900-2
arty-a7-35          xc7a35ticsg324-1L
zybo-z7-10          xc7z010clg400-1
genesys2            xc7k325tffg900-2
nexys_video         xc7a200tsbg484-1
cmod_a7-35t         xc7a35tcpg236-1
cora-z7-10          xc7z010clg400-1
zybo-z7-20          xc7z020clg400-1
eclypse-z7          xc7z020clg484-1
zc702               xc7z020clg484-1
cora-z7-07s         xc7z007sclg400-1
ac701               xc7a200tfbg676-2
arty                xc7a35ticsg324-1L
kcu116              xcku5p-ffvb676-2-e
arty-s7-25          xc7s25csga324-1
zcu106              xczu7ev-ffvc1156-2-e
arty-z7-10          xc7z010clg400-1
zed                 xc7z020clg484-1
zcu104              xczu7ev-ffvc1156-2-e
nexys-a7-50t        xc7a50ticsg324-1L
sp701               xc7s100fgga676-2
nexys4_ddr          xc7a100tcsg324-1
zedboard            xc7z020clg484-1
arty-s7-50          xc7s50csga324-1
zybo                xc7z010clg400-1
arty-z7-20          xc7z020clg400-1
cmod_a7-15t         xc7a15tcpg236-1
arty-a7-100         xc7a100tcsg324-1
nexys-a7-100t       xc7a100tcsg324-1
```

Edit XML files in /path/to/Xilinx/Vivado/20xx.x/data/boards/board_files/ if you want to add/modify boards name.

## License

[MIT License](LICENSE)

Vivado HLS is trademark of Xilinx.

## Contact

Author: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
