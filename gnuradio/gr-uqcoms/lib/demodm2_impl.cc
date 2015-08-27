/* -*- c++ -*- */
/* 
 * Copyright 2013 Konstanty Bialkowski <konstanty@ieee.org>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gr_io_signature.h>
#include "demodm2_impl.h"

namespace gr {
  namespace uqcoms {

    demodm2::sptr
    demodm2::make(unsigned char bits_per_sample, float threshold)
    {
      return gnuradio::get_initial_sptr
        (new demodm2_impl(bits_per_sample, threshold));
    }

    /*
     * The private constructor
     */
    demodm2_impl::demodm2_impl(unsigned char samples_per_bit, float threshold)
      : gr_block("demodm2",
		      gr_make_io_signature(1, 1, sizeof(float)),
		      gr_make_io_signature(1, 1, sizeof(unsigned char))),
        my_samples_per_bit(samples_per_bit),
        my_threshold(threshold)
    {}

    /*
     * Our virtual destructor.
     */
    demodm2_impl::~demodm2_impl()
    {
    }

    void
    demodm2_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        int n = noutput_items * my_samples_per_bit;
        ninput_items_required[0] = (n==0 ? 1 : n);
    }

    int
    demodm2_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        uint8_t *out = (uint8_t *) output_items[0];
        int n_in_items = ninput_items[0];

        int i = 0, o;
        // until we reout of space in the output - or the input.
        for (o=0; o<noutput_items && (i < n_in_items); o++) {

           // for the oth output symbol, lets get out data
           float Ts = my_samples_per_bit; // samples per bit
           float sum[4] = {0, 0, 0, 0}; // 4 parts of the bit.
           for (int z=i; z<i+Ts/4; z++) {
              sum[0] += in[z];
           }
           for (int z=i+Ts/4+1; z<i+Ts/2; z++) {
              sum[1] += in[z];
           }
           for (int z=i+Ts/2+1; z<i+Ts*3/4; z++) {
              sum[2] += in[z];
           }
           for (int z=i+Ts*3/4; z<i+Ts; z++) {
              sum[3] += in[z];
           }
           i += Ts;

           float decide = fabs((sum[0]+sum[2]) - (sum[1]+sum[3]));

           // how to debug an output... NOT recommended if the data rate is high
           // std::cout << decide << "\n";

           // set output (note it is reversed like in the MATLAB/Octave code)
           out[o] = decide > my_threshold ? 0 : 1;
        }
        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (i);

        // Tell runtime system how many output items we produced.
        return o;
    }

  } /* namespace uqcoms */
} /* namespace gr */

