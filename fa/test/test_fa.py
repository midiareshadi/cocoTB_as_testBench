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
    reset_n._log.debug("Reset complete")

@cocotb.test()
async def fa_tester_function(dut):

    # initial = (LogicArray("U"))
    # assert LogicArray(dut.io_sum.value) == initial
    # assert LogicArray(dut.io_cout.value) == initial

    reset_n = dut.reset
    reset_thread = cocotb.start_soon(reset_dut(reset_n, duration_ns=15))

    dut.io_a.value = 0
    dut.io_b.value = 0
    dut.io_cin.value = 0

    # clock generation
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.clk)
    for i in range(2):
        for a in range(2):
            for b in range(2):
                for cin in range(2):
                    dut.io_a.value = a
                    dut.io_b.value = b
                    dut.io_cin.value = cin
                    await RisingEdge(dut.clk)
                    expected_sum = a ^ b ^ cin
                    expected_cout =  (a & b) | (a & cin) | (b & cin)
                    assert dut.io_sum.value == expected_sum, f"output sum was incorrect on the {i}th cycle"
                    assert dut.io_cout.value == expected_cout, f"output cout was incorrect on the {i}th cycle"
                    

    await RisingEdge(dut.clk)
    assert dut.io_sum.value == expected_sum, f"output sum was incorrect on the last cycle"
    assert dut.io_cout.value == expected_cout, f"output cout was incorrect on the last cycle"

def fa_test_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent

    verilog_sources = []
    
    verilog_sources = [proj_path / "fa.v"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="fa",
        always=True,
    )

    runner.test(hdl_toplevel="fa", test_module="test_fa,")

if __name__ == "__main__":
    fa_test_runner()