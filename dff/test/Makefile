# cocoTB Makefile

TOPLEVEL_LANG ?= verilog

# PWD=$(shell pwd)

# export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

VERILOG_SOURCES = $(shell pwd) ../hdl/dff.v

MODULE = test_dff
TOPLEVEL = dff

include $(shell cocotb-config --makefiles)/Makefile.sim
