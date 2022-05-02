module adder32_abstracted(
   result, 
   a, b
);

   input[15:0] a;
   input[15:0] b;
   output [15:0] result;
   wire [16:0] sum = {1'b0,a} + {1'b0,b};
   assign      result = sum[16] ? sum[16:1]: sum[15:0];
endmodule 