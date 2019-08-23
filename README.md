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
    list         List usable boards
    create       Create Makefile and tcl scripts

optional arguments:
  -h, --help     show this help message and exit
```

Subcommands `list` and `create` are usable.

### vivado_hls_create_project create

Enter project name (sample) and a board name (Xilinx_ZedBoard) as follows.

```
$ vivado_hls_create_project create sample -b Xilinx_ZedBoard
```

sample directory is generated and Makefile and tcl scripts are generated under the directory.

```
$ tree sample
sample
├── Makefile
├── directives.tcl
├── include
├── scripts
│   ├── cosim.tcl
│   ├── csim.tcl
│   ├── csynth.tcl
│   ├── export.tcl
│   └── init.tcl
├── src
└── test
    ├── include
    └── src

6 directories, 7 files
```

See `create -h` for more options.

### vivado_hls_create_project list

`list` shows boards name that can be specified with `create` subcommand.

```
$ vivado_hls_create_project list
Board               Part
--------------------------------------------------
Alpha-Data          xc7vx690tffg1157-2
KU_Alphadata        xcku060-ffva1156-2-e
Xilinx_ZedBoard     xc7z020clg484-1
Xilinx_AC701        xc7a200tfbg676-2
Xilinx_KC705        xc7k325tffg900-2
Xilinx_KCU105       xcku040-ffva1156-2-e
Xilinx_KCU116       xcku5p-ffvb676-2-e
Xilinx_KCU1500      xcku115-flvb2104-2-e
Xilinx_VC707        xc7vx485tffg1761-2
Xilinx_VC709        xc7vx690tffg1761-2
Xilinx_VCU108       xcvu095-ffva2104-2-e
Xilinx_VCU110       xcvu190-flgc2104-2-e
Xilinx_VCU118       xcvu9p-flga2104-2L-e
Xilinx_VCU1525      xcvu9p-fsgd2104-2L-e
Xilinx_ZC702        xc7z020clg484-1
Xilinx_ZC706        xc7z045ffg900-2
Xilinx_ZCU102       xczu9eg-ffvb1156-2-i
Xilinx_ZCU106       xczu7ev-ffvc1156-2-i-es2
Xilinx_A-U200       xcu200-fsgd2104-2-e
Xilinx_A-U250       xcu250-figd2104-2L-e
```

Edit XML files in /path/to/Xilinx/Vivado/20xx.x/data/boards/board_files/ if you want to add/modify boards name.

## License

[MIT License](LICENSE)

Vivado HLS is trademark of Xilinx.

## Contact

Author: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
