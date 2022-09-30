import numpy as np


def int2bit(x, nbits=8, ismsb=True):
    bitorder = 'big' if ismsb else 'little'

    if nbits > 8 and nbits // 8 * 8 != nbits:
        raise ValueError('nbits must be less than or equal to 8 (or a multiple of 8)')
    if nbits > 8:
        # convert to bytes
        if isinstance(x, list) or isinstance(x, np.ndarray):
            xx_array = np.zeros((len(x), nbits//8), dtype=np.uint8)
            for xidx, xx in enumerate(x):
                xx = xx.to_bytes(nbits // 8, byteorder=bitorder)
                xx = np.frombuffer(xx, dtype=np.uint8)
                xx_array[xidx, :] = xx
            x = xx_array
        else:
            x = x.to_bytes(nbits // 8, byteorder=bitorder)
            x = np.frombuffer(x, dtype=np.uint8)

    symbits = np.array(x, dtype=np.uint8).reshape((-1, 1))
    unpackbits = np.unpackbits(np.array(symbits, dtype=np.uint8), axis=1, bitorder=bitorder)[-nbits:]
    if nbits > 8:
        return unpackbits.reshape(-1, nbits)
    return unpackbits


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

