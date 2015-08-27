#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr

class demodm2(gr.basic_block):
    my_threshold = 0
    my_samples_per_bit = 0
    """
    docstring for block demodm2
    """
    def __init__(self, samples_per_bit, threshold):
        gr.basic_block.__init__(self,
            name="demodm2",
            in_sig=[numpy.float32],
            out_sig=[numpy.int8])
        self.my_threshold = threshold
        self.my_samples_per_bit = samples_per_bit

    def forecast(self, noutput_items, ninput_items_required):
        n = noutput_items * self.my_samples_per_bit
        ninput_items_required[0] = 1 if (n==0) else n

    def general_work(self, input_items, output_items):
        inp = input_items[0]
        i = 0
        # until we run-out of space in the output - or the input.
        for o in range(min(len(input_items[0]), len(output_items[0]))):
           # for the oth output symbol, lets get out data
           Ts = self.my_samples_per_bit # samples per bit
           tsum = [0, 0, 0, 0]; # 4 parts of the bit.
           for z in range(i, i+Ts/4):
              tsum[0] += inp[z]
           for z in range(i+Ts/4+1, i+Ts/2):
              tsum[1] += inp[z]
           for z in range(i+Ts/2+1, i+Ts*3/4):
              tsum[2] += inp[z]
           for z in range(i+Ts*3/4, i+Ts):
              tsum[3] += inp[z]

           i += Ts;

           decide = numpy.abs((tsum[0]+tsum[2]) - (tsum[1]+tsum[3]));

           # how to debug an output... NOT recommended if the data rate is high
           # print "%d\n" % decide

           # set output (note it is reversed like in the MATLAB/Octave code)
           output_items[0][o] = 0 if decide > self.my_threshold else 1;

        return len(output_items[0])
