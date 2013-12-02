clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% input dei dati
dat_aria_press = csvread("../Dati/aria.csv")(2:end, 1);
dat_aria_prima = csvread("../Dati/aria.csv")(2:end, 2);
dat_aria_seconda = csvread("../Dati/aria.csv")(2:end, 3);
dat_aria_terza = csvread("../Dati/aria.csv")(2:end, 4);
dat_aria_quarta = csvread("../Dati/aria.csv")(2:end, 5);
dat_vetro_angolo = csvread("../Dati/vetro.csv")(2:end, 1);
dat_vetro_prima = csvread("../Dati/vetro.csv")(2:end, 2);
dat_vetro_seconda = csvread("../Dati/vetro.csv")(2:end, 3);

% elaborazione dati
Press = ones(length(dat_aria_press),1).*1000 .+ dat_aria_press; % [mbar]
dPress = 20; % [mbar]
N = (mean([dat_aria_prima'; dat_aria_seconda'; dat_aria_terza'; dat_aria_quarta']))';
%dN = fallo tu pasa dato che sei fugo

% altri dati
D = 32.5; % [mm] spessore camera a vuoto
%dD = 
t = 5.75; % [mm] spessore vetro
lambda = 543.5; % [um] lambda del laser verde

% pulisco la lista variabili % O FORSE NO?
% clear dat_aria_press dat_aria_prima dat_aria_terza dat_aria_quarta dat_vetro_angolo dat_vetro_prima dat_vetro_seconda;

% analisi dati

DeltaN = N.*lambda ./ (2 *D); % non ho idea di quello che sto scrivendo
% da cui si ricava N0
nPatm = 1 + N0.*lambda ./ (2 *D);