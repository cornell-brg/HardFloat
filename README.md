PyMTL3 Wrappers of BSG Hardfloat
================================

This branch hosts the PyMTL3 wrappers of BSG Hardfloat modules. We used
the BSG modules in the HB tapeout for consistency and better design
quality (e.g., their repos incorporate a few bug fixes and improvements).

Package Overview for Berkeley HardFloat Release 1
=================================================

John R. Hauser
2019 July 29

Berkeley HardFloat is a hardware implementation of binary floating-point
that conforms to the IEEE Standard for Floating-Point Arithmetic.  This
version of HardFloat is encoded in Verilog.  Additional sources are included
for testing HardFloat through simulation.

The HardFloat package is documented in the following files in the "doc"
subdirectory:

    HardFloat-Verilog.html         Documentation for the HardFloat modules.
    HardFloat-test-Verilog.html    Documentation for testing HardFloat using
                                    Verilog simulation
    HardFloat-test-Verilator.html  Documentation for testing HardFloat using
                                    Verilator

Other files in the package comprise the source code for HardFloat and
associated testing infrastructure.

