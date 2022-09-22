import numpy as np


def int2bit(x, nbits=8, ismsb=True):
    symbits = np.array(x, dtype=np.uint8).reshape((-1,1))
    bitorder = 'big' if ismsb else 'little'
    return np.unpackbits(np.array(symbits, dtype=np.uint8), axis=1, bitorder=bitorder)[:,-nbits:]


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

