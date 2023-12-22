import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray


@cocotb.test()
async def dff_simple_test(dut):

    initial = (
        LogicArray("U")
    )
    assert LogicArray(dut.q.value) == initial
    
    dut.d.value = 0

    clock = Clock(dut.clk, 10, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.clk)
    expected_val = 0  
    for i in range(10):
        for j in range(2):
            val = j
            dut.d.value = val 
            await RisingEdge(dut.clk)
            assert dut.q.value == expected_val, f"output q was incorrect on the {i}th cycle"
            expected_val = val  

    await RisingEdge(dut.clk)
    assert dut.q.value == expected_val, "output q was incorrect on the last cycle"

def test_simple_dff_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent

    verilog_sources = []
    
    verilog_sources = [proj_path / "dff.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="dff", test_module="test_dff,")

if __name__ == "__main__":
    test_simple_dff_runner()