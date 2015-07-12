%                        The University of Queensland
%     School of Information Technology & Electrical Engineering
%		COMS4105/COMS7410 Communication Systems

% Plot the capacity of a binary symmetric channel
alpha = 0.02:0.02:0.98;
C = 1 + alpha .* log2(alpha) + (1-alpha) .* log2(1-alpha);
% Note that we leave out alpha = 0 & alpha = 1.  This is because as x->0,
% the mathematical limit of x log x is 0 but Matlab returns NaN for the
% logarithm operation.  Hence, we insert these limit cases separately.
plot([0, alpha, 1], [1, C, 1]);
xlabel('\alpha');
ylabel('C_2 (bits per channel use)');
