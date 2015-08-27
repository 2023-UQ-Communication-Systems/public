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

#ifndef INCLUDED_UQCOMS_DEMODM2_IMPL_H
#define INCLUDED_UQCOMS_DEMODM2_IMPL_H

#include <gnuradio/gr_complex.h>
#include <uqcoms/demodm2.h>

namespace gr {
  namespace uqcoms {

    class demodm2_impl : public demodm2
    {
     private:
      // local variables
      unsigned char my_samples_per_bit;
      float my_threshold;

     public:
      demodm2_impl(unsigned char bits_per_sample, float threshold);
      ~demodm2_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace uqcoms
} // namespace gr

#endif /* INCLUDED_UQCOMS_DEMODM2_IMPL_H */

