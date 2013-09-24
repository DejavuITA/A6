# importa roba inutile di Dave
source("../../algoritmi/alg1.m");

# input dei dati
dati = csvread("../Dati/dati.csv");

# separa i dati
pompate = dati(2:end, 1);
pressioni = mmhg_to_pa(730 - dati(2:end, 2));
log_pressioni = log(pressioni);