% From MATLAB 2021b onwards, Mathworks recommends not using de2bi
% and instead use int2bit.
% However octave does not have this function, so we wrap around de2bi.
% Here is a small (mostly) compatible version of this.
function [out] = int2bit(input, nbits, msbfirst)
	order = 'left-msb';
	if (msbfirst == false)
	    order = 'right-msb';
	end
	out = transpose(de2bi(input, nbits, order));
