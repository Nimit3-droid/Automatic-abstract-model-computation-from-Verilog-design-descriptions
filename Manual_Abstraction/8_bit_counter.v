module up_counter (

    out      ,  // Output of the counter
    clk      ,  // clock input
    data     ,  // Data to load
    reset       // reset input
);

output [7:0] out;
input [7:0] data;
input clk, reset;
reg [7:0] out;

always @(posedge clk)

if (reset) 
    begin // active high reset
        out <= 8'b0 ;
    end 
else 
    begin
        out <= out + 1;
    end
endmodule