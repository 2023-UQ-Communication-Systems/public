%% Rayleigh

% Simulation
Nsamples = 10e5;
I = randn(1, Nsamples);
Q = randn(1, Nsamples);

Z = I + j*Q;

% Get histogram data for simulation
step = 0.1;
zRange = 0:step:7;
hold off;
[raysim zx] = hist(abs(Z), zRange);

% Theory
var = 1;
RayleighTheory = zeros(size(zRange));
for (zi=1:length(zRange))
    z = zRange(zi);
    RayleighTheory(zi) = z/var * exp(- (z^2)/(2*var));
end

% Plot both Theory and Simulation
plot(zx, raysim/Nsamples/step, 'bx');
hold on;
plot(zRange, RayleighTheory, 'r');