SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/../hdl/FIFO2.v
VERILOG_SOURCES += $(PWD)/wrappers/intf_test.v

intf:
		rm -rf sim_build
		$(MAKE) sim MODULE=intf_test TOPLEVEL=intf_test
	
include $(shell cocotb-config --makefiles)/Makefile.sim