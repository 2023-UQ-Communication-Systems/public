import numpy as np


def int2bit(x, nbits=8, ismsb=True):
    '''Convert data from packed to unpacked'''
    bitorder = 'big' if ismsb else 'little'

    if nbits > 8 and nbits // 8 * 8 != nbits:
        raise ValueError('nbits must be less than or equal to 8 (or a multiple of 8)')

    outbits = np.zeros(nbits * len(x), dtype=np.uint8)
    for xidx, xdata in enumerate(x):
        for jj in range(nbits):
            if bitorder == 'little':
                outbits[xidx * nbits + jj] = (xdata >> (nbits - jj - 1)) & 1
            else:
                outbits[xidx * nbits + jj] = (xdata >> jj) & 1

    return outbits


def bit2int(x, nbits=8, ismsb=True):
    if nbits > 8:
        raise ValueError('nbits must be less than or equal to 8')
    bitorder = 'big' if ismsb else 'little'
    # pad each row with zeros at the start of each row
    x = np.reshape(x, (-1, nbits))

    if bitorder == 'little':
        x = np.fliplr(x)
    x = np.pad(x, ((0, 0), (8 - nbits, 0)), 'constant')  # padding required to use packbits
    if bitorder == 'little':
        x = np.fliplr(x)
    return np.packbits(x, bitorder=bitorder, axis=1)

# Utility functions to mimic MATLAB's int2bit/bit2int

