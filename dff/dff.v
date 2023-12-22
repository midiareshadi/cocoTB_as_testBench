`timescale 1ns/1ns

module dff (
  input logic clk, d,
  output logic q
);

always @(posedge clk) begin
  q <= d;
end

  // Dump VCD
  initial begin
    $dumpfile("VCD_File.vcd");
    $dumpvars;
  end

endmodule
