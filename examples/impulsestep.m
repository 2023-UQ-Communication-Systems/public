%		     The University of Queensland
%     School of Information Technology & Electrical Engineering
%	         COMS4105/7410 Digital Communications

% Generate a plot of a discrete-time impulse and a continuous-time step

% Time base for the discrete-time impulse

n = -4:4;

% Compute the discrete-time impulse

delta = zeros(size(n));
i = find(n == 0);
delta(i) = ones(size(i));

% Plot the discrete-time impulse

clf;
subplot(1, 2, 1);
stem(n, delta, 'filled', 'm');
xlabel('Time \itn');
ylabel('\it\delta\rm[\itn\rm]');
ylim([0, 1.5]);

% Time base for the continuous-time step signal

t = -1:0.01:1;

% Compute the continuous-time step signal

u = zeros(size(t));
i = find(t >= 0);
u(i) = ones(size(i));

% Plot the continuous-time step

subplot(1, 2, 2);
plot(t, u);
xlabel('Time \itt');
ylabel('\itu\rm(\itt\rm)');
ylim([0, 1.5]);
