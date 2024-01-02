# cocoTB Makefile

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES = $(shell pwd) ../hdl/Adder4Module.v

MODULE = test_4bitAdder
TOPLEVEL = Adder4Module

include $(shell cocotb-config --makefiles)/Makefile.sim
