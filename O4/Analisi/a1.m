clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% input dei dati
dat_aria_press = csvread("../Dati/aria.csv")(2:(end -1), 1);
dat_aria_prima = csvread("../Dati/aria.csv")(2:(end -1), 2);
dat_aria_seconda = csvread("../Dati/aria.csv")(2:(end -1), 3);
dat_aria_terza = csvread("../Dati/aria.csv")(2:(end -1), 4);
dat_aria_quarta = csvread("../Dati/aria.csv")(2:(end -1), 5);
dat_vetro_angolo = csvread("../Dati/vetro.csv")(2:end, 1);
dat_vetro_prima = csvread("../Dati/vetro.csv")(2:end, 2);
dat_vetro_seconda = csvread("../Dati/vetro.csv")(2:end, 3);

% elaborazione dati
Press = ones(length(dat_aria_press),1).*1000 .+ dat_aria_press; % [mbar]
Press = 100 .* Press; % [Pa]
dPress = 20; % [mbar]
dPress = ones(length(Press),1) .* dPress .* 100; % [Pa]
N = (mean([dat_aria_prima'; dat_aria_seconda'; dat_aria_terza'; dat_aria_quarta']))'; % [#]
dN = [std([dat_aria_prima'; dat_aria_seconda'; dat_aria_terza'; dat_aria_quarta'])]'; % [#]
%N=N.*1.247227; wtf
theta = dat_vetro_angolo .- dat_vetro_angolo(1); % [° -->]
theta = theta.*pi./180; % [--> radianti]
dtheta = ones(length(theta),1) .* 0.05 .* sqrt(2); % [° -->]
dtheta = dtheta.*pi./180; % [--> radianti]

M = (mean([dat_vetro_prima'; dat_vetro_seconda']))';
dM = [std([dat_vetro_prima'; dat_vetro_seconda'])]';
% serie singole
M1 = dat_vetro_prima;
M2 = dat_vetro_seconda;
dM1 = std(dat_vetro_prima);
dM2 = std(dat_vetro_seconda);

% altri dati
D = 32.5.*(10^-3); % [m] spessore camera a vuoto
dD = 1e-3;  #0.05.*(10^-3); % [m]
t = 5.75.*(10^-3); % [m] spessore vetro
dt = 0.05.*(10^-3); % [m]
lambda = 543.5.*(10^-9); % [m] lambda del laser verde

% pulisco la lista variabili
clear ans dat_aria_press dat_aria_prima dat_aria_terza dat_aria_quarta dat_vetro_angolo dat_vetro_prima dat_vetro_seconda;

% analisi dati 1

An = N.*lambda ./ (2 *D); % non ho idea di quello che sto scrivendo
dAn = sqrt((dN.*lambda ./ (2 .* D)).^2 .+ (N.*lambda ./ (2 .* D.^2) .* dD).^2);
% da cui si ricava N0... presumo...
[A B dA dB] = fit(N, Press, (dN .+ ones(length(N),1)).^-2);
N_0 = A;
dN_0 = dA;

[nA nB dnA dnB] = fit(An, Press, dAn.^-2);
1 + nA
dnA

n_Patm = 1 + N_0.*lambda ./ (2 * D)
dn_Patm = ((lambda./(2.*D).*dN_0).^2 .+ (N_0.*lambda./2./(D^2).*dD).^2)^0.5

% analisi dati 2

% vettorizzo tutto
% altri dati
%t = 5.75.*(10^-3).*ones(18,1); % [m] spessore vetro
%dt = 0.005.*(10^-3).*ones(18,1); % [m] ?
%lambda = 543.5.*(10^-9).*ones(18,1); % [m] lambda del laser verde

n  = ((2.*t .- M.*lambda) .* (1 .- cos(theta))) ./ \
	(2.*t.*(1 .- cos(theta)) .- M.*lambda);
% serie singole
n1 = ((2.*t .- M1.*lambda) .* (1 .- cos(theta))) ./ \
	(2.*t.*(1 .- cos(theta)) .- M1.*lambda);
n2 = ((2.*t .- M2.*lambda) .* (1 .- cos(theta))) ./ \
	(2.*t.*(1 .- cos(theta)) .- M2.*lambda);

% l'errore non viene... @_@
sqrt_arg = ((2.*t .- M.*lambda) .* M .* sin(theta) .* dtheta).^2 .+ \
	(2 .* cos(theta) .* (1 - cos(theta))).^2 .* \
	((M .* dt).^2 .+ (t .* dM).^2);
% serie singole
sqrt_arg1 = ((2.*t .- M1.*lambda) .* M1 .* sin(theta) .* dtheta).^2 .+ \
	(2 .* cos(theta) .* (1 - cos(theta))).^2 .* \
	((M1 .* dt).^2 .+ (t .* dM1).^2);
sqrt_arg2 = ((2.*t .- M2.*lambda) .* M2 .* sin(theta) .* dtheta).^2 .+ \
	(2 .* cos(theta) .* (1 - cos(theta))).^2 .* \
	((M2 .* dt).^2 .+ (t .* dM2).^2);

dn = sqrt(sqrt_arg) .* lambda .* ((2 .* t .* (1.-cos(theta)) .- M.*lambda).^(-2));
% serie singole
dn1 = sqrt(sqrt_arg) .* lambda .* ((2 .* t .* (1.-cos(theta)) .- M1.*lambda).^(-2));
dn2 = sqrt(sqrt_arg) .* lambda .* ((2 .* t .* (1.-cos(theta)) .- M2.*lambda).^(-2));

printf('\n');
n_fin = weighted_mean(n(2:end), dn(2:end))
n_fin_Err = weighted_mean_err(dn(2:end))
n_stat_fin = mean([n(2:6); n(8:end)])
n_stat_fin_Err = std([n(2:6); n(8:end)])

% serie singole: 1
printf('\n');
n_fin1 = weighted_mean(n1(2:end), dn1(2:end))
n_fin_Err1 = weighted_mean_err(dn1(2:end))

% serie singole: 2
printf('\n');
n_fin2 = weighted_mean(n2(2:end), dn2(2:end))
n_fin_Err2 = weighted_mean_err(dn2(2:end))