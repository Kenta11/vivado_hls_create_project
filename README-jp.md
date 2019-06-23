# vivado_hls_create_project

English version: [vivado_hls_create_project](README.md)

## 概要

Vivado HLSのプロジェクトを作るための，Makefileとtclスクリプトを自動生成するツールです．

## 準備

- Python3
- ~/.vivado_hls_create_project: 設定ファイル
	- Vivadoのパスを書いておくファイル
	- JSON形式で以下のように記述する

```
{
    "path_to_vivado": "/path/to/Xilinx/Vivado/20xx.x"
}
```

## 基本的な使い方

gitコマンドのように，サブコマンドで使う機能を選択できます．

```
Usage: vivado_hls_create_project [-h|--help] <command> [<args>]

Makefile and tcl scripts generator for Vivado HLS

<command>:
    list         List usable boards
    create       Create Makefile and tcl scripts

optional arguments:
  -h, --help     show this help message and exit
```

listとcreateコマンドが使えます．

### vivado_hls_create_project create

プロジェクト名(sample)とボード名(Xilinx_ZedBoard)を以下のように入力して下さい．

```
$ vivado_hls_create_project create sample -b Xilinx_ZedBoard
```

sampleディレクトリが生成され，以下にはMakefileやtclスクリプトが生成されます．

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

詳細なオプションについては`create -h`を参照して下さい．

### vivado_hls_create_project list

createコマンドで指定できるボード名を確認できます．

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

このボード名を追加または変更したい場合は，/path/to/Xilinx/Vivado/20xx.x/common/config/VivadoHls_boards.xmlを編集して下さい．

## ライセンス

[MIT License](LICENSE)

Vivado HLSはXilinx社の商標です．

## コンタクト

作者: Kenta Arai

Twitter: [@isKenta14](https://twitter.com/isKenta14)
