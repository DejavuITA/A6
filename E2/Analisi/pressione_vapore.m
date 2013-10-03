# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/pressioni_vapore.csv")(2:end, :);

p_atm = 719 * 133.322;
sp_atm = 1 * 133.322;

# pressione 
p = p_atm .+ dati(:, 1);
sp = sqrt(sp_atm^2 + 5000^2/12);
# temperatura
T = 273.15 .+ dati(:, 2);
sT = 1 / sqrt(12);

# preparazione fit
logp = log(p);
slogp = sp./p;
T1 = T .^ -1;
sT1 = -sT./T.^2;

# fit
[A, B, sA, sB] = fit(logp, T1, slogp .^ (-2))

# chi2
chi_square = chi2(logp, T1, slogp, A, B)

# torniamo a valori Clapeyron eq.
p0 = exp(A)
sp0 = exp(A) * sA
DH = - B * 8.3144
sDH = sB * 8.3144

T_ebb = B / (log(101300) - A) - 273.15