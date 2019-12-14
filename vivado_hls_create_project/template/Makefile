##### configuration #####

VIVADO_HLS := $(shell vivado_hls_create_project get-config path_to_vivado)/bin/vivado_hls

# project and solution name
export HLS_TARGET   := {{TARGET}}
export HLS_SOLUTION := {{SOLUTION}}
# source files
HLS_HEADER          := $(wildcard include/*) $(wildcard test/include/*)
export HLS_SOURCE   := $(wildcard src/*)
export HLS_TEST     := $(wildcard test/src/*)

# result
BASE_DIR := $(HLS_TARGET)/$(HLS_SOLUTION)
IP       := $(BASE_DIR)/impl
COSIM    := $(BASE_DIR)/sim
HDL      := $(BASE_DIR)/syn
CSIM     := $(BASE_DIR)/csim

##### targets and commands #####

.PHONY: all
all: $(IP)

.PHONY: export
export: $(IP)
$(IP): $(HDL)
	$(VIVADO_HLS) script/export.tcl

.PHONY: cosim
cosim: $(COSIM)
$(COSIM): $(HDL)
	$(VIVADO_HLS) script/cosim.tcl
	touch $@

.PHONY: csynth
csynth: $(HDL)
$(HDL): $(CSIM)
	$(VIVADO_HLS) script/csynth.tcl
	touch $@

.PHONY: csim
csim: $(CSIM)
$(CSIM): $(HLS_TARGET) $(HLS_SOURCE) $(HLS_TEST) $(HLS_HEADER)
	$(VIVADO_HLS) script/csim.tcl
	touch $@

$(HLS_TARGET):
	$(VIVADO_HLS) script/init.tcl

.PHONY: clean
clean:
	rm -rf $(IP) $(COSIM) $(HDL) $(CSIM) *.log

.PHONY: distclean
distclean:
	rm -rf $(HLS_TARGET)
