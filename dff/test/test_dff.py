import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray

async def reset_dut(reset_n, duration_ns):
    reset_n.value = 1
    await Timer(duration_ns, units="ns")
    reset_n.value = 0
    reset_n._log.debug("*** Reset complete ***")

@cocotb.test()
async def dff_tester_function(dut):

    initial = (
        LogicArray("U")
    )
    assert LogicArray(dut.io_q.value) == initial

    reset_n = dut.reset

    reset_thread = cocotb.start_soon(reset_dut(reset_n, duration_ns=15))

    
    dut.io_d.value = 0

    # clock generation
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.clk)
    expected_val = 0
    for i in range(5):
        for j in range(2):
            val = j
            dut.io_d.value = val 
            await RisingEdge(dut.clk)
            assert dut.io_q.value == expected_val, f"output q was incorrect on the {i}th cycle"
            expected_val = val  

    await RisingEdge(dut.clk)
    assert dut.io_q.value == expected_val, "output q was incorrect on the last cycle"

def dff_test_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent

    verilog_sources = []
    
    verilog_sources = [proj_path / "dff.v"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="dff", test_module="test_dff,")

if __name__ == "__main__":
    dff_test_runner()