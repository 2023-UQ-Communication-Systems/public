/* -*- c++ -*- */

#define UQCOMS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "uqcoms_swig_doc.i"

%{
#include "uqcoms/demodm2.h"
%}


%include "uqcoms/demodm2.h"
GR_SWIG_BLOCK_MAGIC2(uqcoms, demodm2);
