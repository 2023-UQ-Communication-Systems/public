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


#ifndef INCLUDED_UQCOMS_DEMODM2_H
#define INCLUDED_UQCOMS_DEMODM2_H

#include <uqcoms/api.h>
#include <gr_block.h>

namespace gr {
  namespace uqcoms {

    /*!
     * \brief <+description of block+>
     * \ingroup uqcoms
     *
     */
    class UQCOMS_API demodm2 : virtual public gr_block
    {
     public:
      typedef boost::shared_ptr<demodm2> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of uqcoms::demodm2.
       *
       * To avoid accidental use of raw pointers, uqcoms::demodm2's
       * constructor is in a private implementation
       * class. uqcoms::demodm2::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned char samples_per_bit, float threshold);
    };

  } // namespace uqcoms
} // namespace gr

#endif /* INCLUDED_UQCOMS_DEMODM2_H */

