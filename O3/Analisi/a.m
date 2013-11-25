clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% input dei dati
dat_Imax_pow = csvread("../Dati/Imax.csv")(2:end, 1);
dat_Imax_gradi = csvread("../Dati/Imax.csv")(2:end, 2);
dat_Imax_primi = csvread("../Dati/Imax.csv")(2:end, 3);

Imax = mean(dat_Imax_pow)
theta = pi.*(dat_Imax_gradi .+ dat_Imax_primi./60)./180

% altri dati

% pulisco la lista variabili
clear dat_Imax_pow dat_Imax_gradi dat_Imax_primi;







% questo può tornare utile
% inizio analisi% scrivo i dati
% parte 1
%	[ th_max dth_max n dn ]
% parte 2
%	[ th_i dth_i theta dtheta ]
%	th_i_gradi = fix(th_i .*180 ./ pi);
%	th_i_primi = ((th_i .*180 ./ pi) .- th_i_gradi) .*60;
%	th_i_g = th_i_gradi .+ (th_i_primi ./100);
%	dth_i_gradi = fix(dth_i .*180 ./ pi);
%	dth_i_primi = ((dth_i .*180 ./ pi) .- dth_i_gradi) .*60;
%	dth_i_g = dth_i_gradi .+ (dth_i_primi ./100);
%	dth_i_g (1)
%[th_i_g dth_i_g]
%	theta_gradi = fix(theta .*180 ./ pi);
%	theta_primi = ((theta .*180 ./ pi) .- theta_gradi) .*60;
%	theta_g = theta_gradi .+ (theta_primi ./100);
%	dtheta_gradi = fix(dtheta .*180 ./ pi);
%	dtheta_primi = ((dtheta .*180 ./ pi) .- dtheta_gradi) .*60;
%	dtheta_g = dtheta_gradi .+ (dtheta_primi ./100);
%	dtheta_g (1)
%	[th_i_g theta_g]
clear ans;