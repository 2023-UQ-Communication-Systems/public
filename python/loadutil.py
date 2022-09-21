import numpy as np


# Load SDR data from an RTLSDR (8-bit I/Q) file. Normalise the data to
# [-1, 1] and return as a complex array.
# To limit the amount of data loaded, specify MAX_SAMPLES
def read_complex_byte(filename, MAX_SAMPLES=-1):
    data = np.fromfile(filename, dtype=np.dtype('B'), count=MAX_SAMPLES)
    normdata = (np.array(data, dtype=float)-127)/128
    normdata.dtype = complex
    return normdata
