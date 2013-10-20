# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/pesi.csv");

volume = 0.002769;
s_volume = 0.000005;

moist = 0.58;

T = 22 + 273;
s_T = 1 / sqrt(12);

R = 8.3144;

vuoto = dati(2:end, 2)
pieno = dati(2:end, 3)
pressione = dati(2:end, 4)
s_pressione = 10000 / sqrt(12);

# correzione umidita
pressione_H20 = moist * 1.6055e+11 * exp(-4.3883e04 / (8.3144 * T))
pressione(1, 1) = pressione(1, 1) - pressione_H20

massa = pieno .- vuoto
s_massa = 0.0001 / sqrt(6);

# correzione umidita
moli_H2O = (pressione_H20 * volume) ./ (R .* T)
massa_H20 = moli_H2O * 0.018
massa(1, 1) = massa(1, 1) - massa_H20

moli = (pressione .* volume) ./ (R .* T)
s_moli = sqrt((volume ./ (R .* T) * s_pressione) .^ 2 .+
	(pressione ./ (R .* T) * s_volume) .^ 2 .+
	((pressione .* volume) ./ (R .* T .^ 2)) .^ 2)

# correzione umidita
moli(1, 1) = moli(1, 1) - moli_H2O

massa_mol = massa ./ moli;
s_massa_mol = sqrt((s_massa ./ moli) .^ 2 .+
	(massa ./ (moli .^ 2) .* s_moli) .^ 2);
	
[massa_mol * 1000, s_massa_mol * 1000]