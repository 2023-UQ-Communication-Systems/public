import numpy as np


def int2bit(x, nbits=8, ismsb=True):
    symbits = np.array(x, dtype=np.uint8).reshape((-1,1))
    bitorder = 'big' if ismsb else 'little'
    return np.unpackbits(np.array(symbits, dtype=np.uint8), axis=1, bitorder=bitorder)[-nbits:]


def bit2int(x, nbits=8, ismsb=True):
    bitorder = 'big' if ismsb else 'little'
    return np.packbits(x, bitorder=bitorder)

# Utility functions to mimic MATLAB's int2bit/bit2int