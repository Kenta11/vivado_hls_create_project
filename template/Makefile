##### configuration #####

# project and solution name
export HLS_TARGET   = {{TARGET}}
export HLS_SOLUTION = {{SOLUTION}}
# source files
export HLS_SOURCE   = $(wildcard src/*)
export HLS_TEST     = $(wildcard test/src/*)

# result
BASE_DIR = $(HLS_TARGET)/$(HLS_SOLUTION)
IP       = $(BASE_DIR)/impl
COSIM    = $(BASE_DIR)/sim
HDL      = $(BASE_DIR)/syn
CSIM     = $(BASE_DIR)/csim

##### targets and commands #####

.PHONY: all
all: $(IP)

.PHONY: export
export: $(IP)
$(IP): $(HDL)
	vivado_hls script/export.tcl

.PHONY: cosim
cosim: $(COSIM)
$(COSIM): $(HDL)
	vivado_hls script/cosim.tcl

.PHONY: csynth
csynth: $(HDL)
$(HDL): $(CSIM) $(HLS_SOURCE)
	vivado_hls script/csynth.tcl

.PHONY: csim
csim: $(CSIM)
$(CSIM):
	vivado_hls script/csim.tcl

.PHONY: clean
clean:
	rm -rf $(HLS_TARGET) *.log
