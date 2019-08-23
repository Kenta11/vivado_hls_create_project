# vivado_hls_create_project

English version: [vivado_hls_create_project](README.md)

## 概要

Vivado HLSのプロジェクトを作るための，Makefileとtclスクリプトを自動生成するツールです．

## 要件

- Python3
- GNU Make

## vivado_hls_create_projectをインストール

```
$ sudo pip install git+https://github.com/Kenta11/vivado_hls_create_project
$ vivado_hls_create_project set-config path_to_vivado /path/to/Xilinx/Vivado/20xx.x
# /path/to/Xilinx/Vivado/20xx.x にはVivadoへの絶対パスを設定して下さい
```

## 基本的な使い方

gitコマンドのように，サブコマンドで使う機能を選択できます．

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

list，create，set-config，get-configコマンドが使えます．

### vivado_hls_create_project create

プロジェクト名(sample)とボード名(Xilinx_ZedBoard)を以下のように入力して下さい．

```
$ vivado_hls_create_project create -b Xilinx_ZedBoard sample
```

sampleディレクトリが生成され，以下にはMakefileやtclスクリプトが生成されます．

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

詳細なオプションについては`create -h`を参照して下さい．

### vivado_hls_create_project list

createコマンドで指定できるボード名を確認できます．

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

このボード名を追加または変更したい場合は，/path/to/Xilinx/Vivado/20xx.x/data/boards/board_files/下のXMLファイルを編集して下さい．

## ライセンス

[MIT License](LICENSE)

Vivado HLSはXilinx社の商標です．

## コンタクト

作者: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
