source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% input dei dati della prima parte, cioè di theta_max in funzione di lambda - th_0 = 128.31
th_0 = pi.*(128 .+ 31./60)./180;
	dth_0 = pi.*(1./60)./180;
dat_theta_colori_gradi = csvread("../Dati/thetamax.csv")(2:end, 2);
dat_theta_colori_primi = csvread("../Dati/thetamax.csv")(2:end, 3);
th_col = pi.*(dat_theta_colori_gradi .+ dat_theta_colori_primi./60)./180;
	dth_col = pi.*(1./60)./180;

% input dei dati della seconda parte, cioè di theta in funzione di theta_in
dat_theta_rifl_gradi = csvread("../Dati/deviazione.csv")(2:end, 1);
dat_theta_rifl_primi = csvread("../Dati/deviazione.csv")(2:end, 2);
th_rifl = pi.*(dat_theta_rifl_gradi .+ dat_theta_rifl_primi./60)./180;
	dth_rifl = pi.*(1./60)./180;

dat_theta_dev_gradi = csvread("../Dati/deviazione.csv")(2:end, 3);
dat_theta_dev_primi = csvread("../Dati/deviazione.csv")(2:end, 4);
th_dev = pi.*(dat_theta_dev_gradi .+ dat_theta_dev_primi./60)./180;
	dth_dev = pi.*(1./60)./180;

% altri dati
alpha = pi / 3;

%clear [dat_theta_colori_gradi, dat_theta_colori_primi, dat_theta_dev_gradi, dat_theta_dev_primi, dat_theta_rifl_gradi, dat_theta_rifl_primi] ;

% inizio analisi parte 1 (traviamo n in funzione di theta e lambda)
th_max = (th_col .- th_0)
	dth_max = sqrt(dth_col.^2 .+ dth_0^2)
n = (sin((alpha .+ th_max)./2)) ./ (sin(alpha / 2))
	dn = (abs(cos((alpha .+ th_max) ./ 2) .* dth_max)) ./ (2 .* sin(alpha ./ 2))

% inizio analisi parte 2
th_i = (th_rifl .- th_0) ./2;
	dth_i = sqrt(dth_rifl.^2 .+ dth_0^2) ./ 2;
th_d = (th_dev .- th_0);
	dth_d = sqrt(dth_dev.^2 .+ dth_0^2);
th_r = asin(sin(th_i) ./ n(4));
	dth_r = sqrt(((cos(th_i) .* dth_i) .^ 2 .+ (sin(th_i) ./ n(4) .* dn(4)) .^ 2) ./ (n(4) .^ 2 .- sin(th_i) .^ 2));
theta = th_i + asin(n(4) .* sin(alpha .- th_r)) - alpha;
dtheta = sqrt( dth_i .^2 + ((sin(alpha-th_r) .* dn(4)).^2 .+ (n(4) .* cos(alpha .- th_r) .* dth_r).^2) ./ (1 .- (n(4).*sin(alpha .- th_r)).^2 ) );