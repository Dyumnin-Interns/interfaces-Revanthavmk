module intf_test(CLK,
	   RST_N,

	   a_data,
	   a_en,
	   a_rdy,

	   b_data,
	   b_en,
	   b_rdy,

	   y_en,
	   y_data,
	   y_rdy);
  output reg  CLK;
  input  RST_N;

  // action method a
  input  a_data;
  input  a_en;
  output a_rdy;

  // action method b
  input  b_data;
  input  b_en;
  output b_rdy;

  // actionvalue method y
  input  y_en;
  output y_data;
  output y_rdy;
  intf_or dut(
	  .CLK(CLK),
	  .RST_N(RST_N),
	  .a_data(a_data),
	  .a_en(a_en),
	  .a_rdy(a_rdy),
	  .b_data(b_data),
	  .b_en(b_en),
	  .b_rdy(b_rdy),
	  .y_en(y_en),
	  .y_data(y_data),
	  .y_rdy(y_rdy)
  );

<<<<<<< HEAD
=======

>>>>>>> dcf5a71e71c070d33f0293ded8f4028b4695b4f5
  initial begin
	  $dumpfile("intf.vcd");
	  $dumpvars;
	  CLK=0;
	  forever begin
		  #5 CLK=~CLK;
	  end
  end
<<<<<<< HEAD
  endmodule
=======
  endmodule
dut intf(.CLK(CLK),
		 .RST_N(RST_N),

		 .din_value(din_value),
		 .din_en(din_en),
		 .din_rdy(din_rdy),
		 
		 .dout_en(dout_en),
		 .dout_value(dout_value),
		 .dout_rdy(dout_rdy),

		 .len_value(len_value),
		 .len_en(len_en),
		 .len_rdy(len_rdy),

		 .cfg_address(cfg_address),
		 .cfg_data_in(cfg_data_in),
		 .cfg_op(cfg_op),
		 .cfg_en(cfg_en), 
		 .cfg_data_out(cfg_data_out), .cfg_rdy(cfg_rdy));			 
			
	 	initial begin
		$dumpfile("intf.vcd");
		$dumpvars(1);
		CLK=0;
		forever begin
		    #5 CLK=~CLK;	
		
			end	
        end
endmodule
>>>>>>> dcf5a71e71c070d33f0293ded8f4028b4695b4f5
