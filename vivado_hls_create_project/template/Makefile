##### configuration #####

# project and solution name
export HLS_TARGET   = {{TARGET}}
export HLS_SOLUTION = {{SOLUTION}}
# source files
HLS_HEADER          = $(wildcard include/*) $(wildcard test/include/*)
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
	touch $@

.PHONY: csynth
csynth: $(HDL)
$(HDL): $(CSIM)
	vivado_hls script/csynth.tcl
	touch $@

.PHONY: csim
csim: $(CSIM)
$(CSIM): $(HLS_TARGET) $(HLS_SOURCE) $(HLS_TEST) $(HLS_HEADER)
	vivado_hls script/csim.tcl
	touch $@

$(HLS_TARGET):
	vivado_hls script/init.tcl

.PHONY: clean
clean:
	rm -rf $(IP) $(COSIM) $(HDL) $(CSIM) *.log

.PHONY: distclean
distclean:
	rm -rf $(HLS_TARGET)
