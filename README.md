# vivado_hls_create_project

[日本語版](README-jp.md)

## Summary

It generates Makefile and tcl scripts for creating Vivado HLS project.

## Basic Usage

### Generate Makefile and tcl scripts

Type `project name` and `board name`

```
$ vivado_hls_create_project -p `project name` -b `board name`
```

Available `board name` can be shown using `-l` option.

```
$ vivado_hls_create_project -l
Board               Part
----------------------------
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
Basys3              xc7a35t1cpg236-1
Genesys2            xc7k325t2ffg900c-1
Zybo                xc7z010clg400-1
Zybo_Z7_10          xc7z010clg400-1
Zybo_Z7_20          xc7z020clg400-1
```

If you want to add another boards, edit VivadoHls_boards.xml.

### Help

```
$ vivado_hls_create_project -h
usage: vivado_hls_create_project.py [-h] [-p PROJECT] [-b BOARD] [-s SOLUTION]
                                    [-c CLOCK] [-l] [-cpp]

generates Makefile and tcl scripts

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
  -cpp                  generate C++ code
```

## LICENSE

MIT License

## CONTACT

Author: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
