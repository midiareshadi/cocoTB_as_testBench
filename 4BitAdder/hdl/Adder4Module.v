module FullAdderModule(
  input   io_a,
  input   io_b,
  input   io_cin,
  output  io_sum,
  output  io_cout
);
  assign io_sum = io_a ^ io_b ^ io_cin; // @[FullAdder.scala 17:25]
  assign io_cout = io_a & io_b | io_b & io_cin | io_a & io_cin; // @[FullAdder.scala 19:46]
endmodule
module Adder4Module(
  input        clock,
  input        reset,
  input  [3:0] io_A,
  input  [3:0] io_B,
  input        io_Cin,
  output [3:0] io_Sum,
  output       io_Cout
);
  wire  Adder0_io_a; // @[Adder4Bits.scala 17:22]
  wire  Adder0_io_b; // @[Adder4Bits.scala 17:22]
  wire  Adder0_io_cin; // @[Adder4Bits.scala 17:22]
  wire  Adder0_io_sum; // @[Adder4Bits.scala 17:22]
  wire  Adder0_io_cout; // @[Adder4Bits.scala 17:22]
  wire  Adder1_io_a; // @[Adder4Bits.scala 23:22]
  wire  Adder1_io_b; // @[Adder4Bits.scala 23:22]
  wire  Adder1_io_cin; // @[Adder4Bits.scala 23:22]
  wire  Adder1_io_sum; // @[Adder4Bits.scala 23:22]
  wire  Adder1_io_cout; // @[Adder4Bits.scala 23:22]
  wire  Adder2_io_a; // @[Adder4Bits.scala 29:22]
  wire  Adder2_io_b; // @[Adder4Bits.scala 29:22]
  wire  Adder2_io_cin; // @[Adder4Bits.scala 29:22]
  wire  Adder2_io_sum; // @[Adder4Bits.scala 29:22]
  wire  Adder2_io_cout; // @[Adder4Bits.scala 29:22]
  wire  Adder3_io_a; // @[Adder4Bits.scala 35:22]
  wire  Adder3_io_b; // @[Adder4Bits.scala 35:22]
  wire  Adder3_io_cin; // @[Adder4Bits.scala 35:22]
  wire  Adder3_io_sum; // @[Adder4Bits.scala 35:22]
  wire  Adder3_io_cout; // @[Adder4Bits.scala 35:22]
  wire [2:0] s2 = {Adder2_io_sum,Adder1_io_sum,Adder0_io_sum}; // @[Cat.scala 33:92]
  FullAdderModule Adder0 ( // @[Adder4Bits.scala 17:22]
    .io_a(Adder0_io_a),
    .io_b(Adder0_io_b),
    .io_cin(Adder0_io_cin),
    .io_sum(Adder0_io_sum),
    .io_cout(Adder0_io_cout)
  );
  FullAdderModule Adder1 ( // @[Adder4Bits.scala 23:22]
    .io_a(Adder1_io_a),
    .io_b(Adder1_io_b),
    .io_cin(Adder1_io_cin),
    .io_sum(Adder1_io_sum),
    .io_cout(Adder1_io_cout)
  );
  FullAdderModule Adder2 ( // @[Adder4Bits.scala 29:22]
    .io_a(Adder2_io_a),
    .io_b(Adder2_io_b),
    .io_cin(Adder2_io_cin),
    .io_sum(Adder2_io_sum),
    .io_cout(Adder2_io_cout)
  );
  FullAdderModule Adder3 ( // @[Adder4Bits.scala 35:22]
    .io_a(Adder3_io_a),
    .io_b(Adder3_io_b),
    .io_cin(Adder3_io_cin),
    .io_sum(Adder3_io_sum),
    .io_cout(Adder3_io_cout)
  );
  assign io_Sum = {Adder3_io_sum,s2}; // @[Cat.scala 33:92]
  assign io_Cout = Adder3_io_cout; // @[Adder4Bits.scala 40:11]
  assign Adder0_io_a = io_A[0]; // @[Adder4Bits.scala 18:22]
  assign Adder0_io_b = io_B[0]; // @[Adder4Bits.scala 19:22]
  assign Adder0_io_cin = io_Cin; // @[Adder4Bits.scala 20:17]
  assign Adder1_io_a = io_A[1]; // @[Adder4Bits.scala 24:22]
  assign Adder1_io_b = io_B[1]; // @[Adder4Bits.scala 25:22]
  assign Adder1_io_cin = Adder0_io_cout; // @[Adder4Bits.scala 26:17]
  assign Adder2_io_a = io_A[2]; // @[Adder4Bits.scala 30:22]
  assign Adder2_io_b = io_B[2]; // @[Adder4Bits.scala 31:22]
  assign Adder2_io_cin = Adder1_io_cout; // @[Adder4Bits.scala 32:17]
  assign Adder3_io_a = io_A[3]; // @[Adder4Bits.scala 36:22]
  assign Adder3_io_b = io_B[3]; // @[Adder4Bits.scala 37:22]
  assign Adder3_io_cin = Adder2_io_cout; // @[Adder4Bits.scala 38:17]
endmodule
