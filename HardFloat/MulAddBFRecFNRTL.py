#=========================================================================
# Wrapper for HardFloat's multiplication module
#=========================================================================
# This module supports bfloat16 mul and accumulates into an FP32.

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

from .MulAddRecFNRTL import MulAddRecFN
from .RecFNToFNRTL import RecFNToFN

class MulAddBFRecFN( Component ):

  # Constructor

  def construct( s, expWidth=8, sigWidthBF=8, sigWidthFP=24, imulEn=0 ):

    # Interface

    s.control        = InPort ()
    s.op             = InPort ( 3 )
    s.a              = InPort ( expWidth + sigWidthBF + 1 )
    s.b              = InPort ( expWidth + sigWidthBF + 1 )
    s.c              = InPort ( expWidth + sigWidthFP + 1 )
    s.roundingMode   = InPort ( 3 )

    s.out            = OutPort ( expWidth + sigWidthFP + 1 )
    s.exceptionFlags = OutPort ( 5 )
    s.out_imul       = OutPort ( expWidth + sigWidthFP )

    # Components

    s.hardfloat_fmadd = MulAddRecFN( expWidth, sigWidthFP, imulEn )

    # Connections

    s.a_fp32 = Wire( expWidth + sigWidthFP + 1 )
    s.b_fp32 = Wire( expWidth + sigWidthFP + 1 )

    widthDiff = sigWidthFP - sigWidthBF
    conv_pad_zeros = mk_bits( widthDiff )( 0 )

    # Create a recoded 32 bit floating point number by appending zeros.
    # DC should be able to optimize unused part of the fmadd away.

    @update
    def hf_fmadd_conv():
      s.a_fp32 @= concat( s.a, conv_pad_zeros )
      s.b_fp32 @= concat( s.b, conv_pad_zeros )

    s.hardfloat_fmadd.control        //= s.control
    s.hardfloat_fmadd.op             //= s.op
    s.hardfloat_fmadd.a              //= s.a_fp32
    s.hardfloat_fmadd.b              //= s.b_fp32
    s.hardfloat_fmadd.c              //= s.c
    s.hardfloat_fmadd.roundingMode   //= s.roundingMode
    s.hardfloat_fmadd.out            //= s.out
    s.hardfloat_fmadd.exceptionFlags //= s.exceptionFlags
    s.hardfloat_fmadd.out_imul       //= s.out_imul

    # Only have these converters for debugging purposes
    # s.fp32_out = Wire( expWidth + sigWidthFP )
    # s.conv_c = RecFNToFN( expWidth, sigWidthFP )
    # s.conv_c.in_ //= s.out
    # s.conv_c.out //= s.fp32_out

    # s.fp32_a = Wire( expWidth + sigWidthFP )
    # s.conv_a = RecFNToFN( expWidth, sigWidthFP )
    # s.conv_a.in_ //= s.a_fp32
    # s.conv_a.out //= s.fp32_a

    # s.fp32_b = Wire( expWidth + sigWidthFP )
    # s.conv_b = RecFNToFN( expWidth, sigWidthFP )
    # s.conv_b.in_ //= s.b_fp32
    # s.conv_b.out //= s.fp32_b
