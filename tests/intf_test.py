import cocotb
from cocotb.triggers import (Event, RisingEdge, ReadOnly, Timer, NextTimeStep, Edge)
from cocotb_bus.drivers import BusDriver


def sb_fn(actual_value):
    global exp_value
    assert actual_value == exp_value.pop(0), "Scoreboard Matching Failed"


@cocotb.test()
async def intf_test(dut):
    global exp_value
    a = (0,0,1,1)
    b = (0,1,0,1)
    exp_value = [0,1,1,1]

    dut.RST_N.value = 1
    await Timer(1, 'ns')
    dut.RST_N.value = 0
    await Timer(1, 'ns')
    await RisingEdge(dut.CLK)
    dut.RST_N.value = 1

    adrv = InputDriver(dut, 'a', dut.CLK)
    bdrv = InputDriver(dut, 'b', dut.CLK)
    OutputDriver(dut, 'y', dut.CLK, sb_fn)

    for i in range(4):
        adrv.append(a[i])
        bdrv.append(b[i])
    while len(exp_value)>0:
        await Timer(2,'ns')

class InputDriver(BusDriver):
    _signals = ["rdy", "en", "data"]

    def __init__(self, dut, name, CLK):
        BusDriver.__init__(self, dut, name, CLK)
        self.bus.en.value= 0
        self.CLK = CLK
        

    async def _driver_send(self,value,sync=True):
        if self.bus.rdy.value != 1:
            await RisingEdge(self.bus.rdy)
        self.bus.en.value = 1
        self.bus.data.value = value
        await ReadOnly()
        await RisingEdge(self.CLK)
        self.bus.en.value = 0
        await NextTimeStep()

class OutputDriver(BusDriver):
    _signals = [ 'rdy', 'en', 'data']

    def __init__(self, dut, name, CLK, sb_callback):
        BusDriver.__init__(self, dut, name, CLK)
        self.bus.en.value = 0
        self.CLK = CLK
        self.callback = sb_callback
        self.append(0)

    async def _driver_send(self,value,sync=True):
        while True:
            if self.bus.rdy.value != 1:
                await RisingEdge(self.bus.rdy)
            self.bus.en.value  = 1
            await ReadOnly()
            self.callback(self.bus.data.value)
            await RisingEdge(self.CLK)
            await NextTimeStep()
            self.bus.en.value = 0
