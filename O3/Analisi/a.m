clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% input dei dati
dat_Int_max_pow = csvread("../Dati/imax.csv")(2:end, 1);
dat_Int_max_gradi = csvread("../Dati/imax.csv")(2:end, 2);
dat_Int_max_primi = csvread("../Dati/imax.csv")(2:end, 3);
dat_dat_pow = csvread("../Dati/dati.csv")(2:end, 1);
dat_dat_gradi = csvread("../Dati/dati.csv")(2:end, 2);
dat_dat_primi = csvread("../Dati/dati.csv")(2:end, 3);

Int_max = mean(dat_Int_max_pow)
theta_max = mean(pi.*(dat_Int_max_gradi .+ dat_Int_max_primi./60)./180)
Int = dat_dat_pow;
theta = pi.*(dat_dat_gradi .+ dat_dat_primi./60)./180;

% altri dati

% pulisco la lista variabili
clear dat_Int_max_pow dat_Int_max_gradi dat_Int_max_primi dat_dat_pow dat_dat_gradi dat_dat_primi;

% analisi dati
Int_rel = Int ./ Int_max
%x = sin(theta);


%[Int_rel x]
New_Int = [Int_rel' 1]'; % :-) cmq bastava mettere ; al posto di spazio senza trasporre nulla
New_theta = [theta' theta_max]' .- theta_max;
x = sin(New_theta);
New_Int = [New_Int(45)' New_Int(1:25)' New_Int(26:44)']';
x = [x(45)' x(1:25)' x(26:44)']';
New_theta = [New_theta(45)' New_theta(1:25)' New_theta(26:44)']';
[New_Int x]
 
 % non so cosa faccio Andrea
dy = 0.001
% questi due sotto non c'entrano nulla
%d_y_1 = sqrt((1./Int.^2)*(dx^2))
%d_y_2 = sqrt((((theta./(Int.^2)).^2)*(dy^2)))
% errore sulle y relative.
dy_tot = sqrt((1/Int_max^2)*(dy^2).+(((Int./(Int_max^2)).^2)*(dy^2)))

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