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
dPress = 20; % [mbar]
N = (mean([dat_aria_prima'; dat_aria_seconda'; dat_aria_terza'; dat_aria_quarta']))'; % [#]
dN = [std([dat_aria_prima'; dat_aria_seconda'; dat_aria_terza'; dat_aria_quarta'])]'; % [#]

theta = dat_vetro_angolo .- dat_vetro_angolo(1); % theta in radianti o in gradi?
dtheta = ones(length(theta),1) .* 0.005 .* sqrt(2);
M = (mean([dat_vetro_prima'; dat_vetro_seconda']))';
dM = [std([dat_vetro_prima'; dat_vetro_seconda'])]';

% altri dati
D = 32.5; % [mm] spessore camera a vuoto
%dD = 
t = 5.75; % [mm] spessore vetro
%dt =
lambda = 543.5; % [um] lambda del laser verde

% pulisco la lista variabili % O FORSE NO?
% clear ans dat_aria_press dat_aria_prima dat_aria_terza dat_aria_quarta dat_vetro_angolo dat_vetro_prima dat_vetro_seconda;

% analisi dati 1

AN = N.*lambda./1000 ./ (2 *D); % non ho idea di quello che sto scrivendo
% da cui si ricava N0... presumo...
[A B dA dB] = fit(N, Press,(ones(length(N),1).*0.5).^-2);
N0 = A;

nPatm = 1 + N0.*lambda./1000 ./ (2 *D)

% analisi dati 2
plot (theta,M)