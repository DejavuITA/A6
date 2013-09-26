# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/dati.csv");

# separa i dati
pompate = dati(2:end, 1);
pressioni = mmhg_to_pa(730 - dati(2:end, 2));
log_pressioni = log(pressioni .- 10000);

[b, A, sb, sA] = fit(log_pressioni, pompate, ones(length(pompate), 1))
B = exp(b)