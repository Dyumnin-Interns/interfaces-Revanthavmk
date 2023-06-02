SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/../hdl/FIFO2.v
VERILOG_SOURCES += $(PWD)/wrappers/intf_test.v

intr:
		
		$(MAKE) sim MODULE=intf_test TOPLEVEL=-s dut.v
		$(MAKE) sim MODULE=intf_test TOPLEVEL=FIFO2.v
include $(shell cocotb-config --makefiles)/Makefile.sim