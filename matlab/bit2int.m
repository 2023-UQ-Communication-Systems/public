% From MATLAB 2021b onwards, Mathworks recommends not using bi2de
% and instead using bit2int.
% However octave does not have this function, so we wrap around bi2de
% Here is a small (mostly) compatible version of this.
function [X] = bit2int(Y, n, msbfirst)
	order = 'left-msb';
	if (msbfirst == false)
	    order = 'right-msb';
	end
	Ysize = size(Y);
	Ypad = resize(Y, n, Ysize(2));
	X = transpose(bi2de(logical(transpose(Ypad)), 2, order));
