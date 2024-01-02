import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray

import sys
sys.path.insert(0, '../model')
from python_model import *


async def reset_dut(reset_n, duration_ns):
    reset_n.value = 1
    await Timer(duration_ns, units="ns")
    reset_n.value = 0
    reset_n._log.debug("Reset complete")


@cocotb.test()
async def Adder4_tester_function(dut):

    reset_n = dut.reset
    reset_thread = cocotb.start_soon(reset_dut(reset_n, duration_ns=15))

    dut.io_A.value = 0
    dut.io_B.value = 0
    dut.io_Cin.value = 0

    # clock generation
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.clk)
    for i in range(16):
        for A in range(16):
            for B in range(16):
                dut.io_A.value = A
                dut.io_B.value = B
                await RisingEdge(dut.clk)
                expected_Sum, expected_Cout = Bit4Adder_python_model(A, B, 0)
                assert dut.io_Sum.value == expected_Sum, f"output sum was incorrect on the {i}th cycle"
                assert dut.io_Cout.value == expected_Cout, f"output cout was incorrect on the {i}th cycle"
                    

    await RisingEdge(dut.clk)
    assert dut.io_Sum.value == expected_Sum, f"output sum was incorrect on the last cycle"
    assert dut.io_Cout.value == expected_Cout, f"output cout was incorrect on the last cycle"

def adder4_test_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent

    verilog_sources = []
    
    verilog_sources = [proj_path / "Adder4Module.v"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="Adder4Module",
        always=True,
    )

    runner.test(hdl_toplevel="Adder4Module", test_module="test_Adder4Module,")

if __name__ == "__main__":
    adder4_test_runner()