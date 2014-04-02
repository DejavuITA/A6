clear Local user variables;

source("../../../algoritmi/alg1.m");
source("../../../algoritmi/utils.m");

mill = csvread("../dati/dati.csv")(2:(end), 1);
siem = csvread("../dati/dati.csv")(2:(end), 2);
dmill = ones(length(mill),1).*0.1/sqrt(12);
dsiem = ones(length(siem),1).*0.01/sqrt(12);

display("");

%[mill dmill siem dsiem]

% fit preliminari
display("fit preliminari");
w = dsiem.^(-2);
[A1 B1 sA1 sB1] = fit(siem(1:13), mill(1:13), w(1:13)) % w = dy.^(-2)
display("");
[A2 B2 sA2 sB2] = fit(siem(14:end), mill(14:end), w(14:end)) % w = dy.^(-2)

display("");display("");

% fit con incertezza x trasferita
display("fit secondari");
dy1_tot = sqrt(dsiem.^2+B1^2*dmill.^2);
w1_tot = dy1_tot.^(-2);
[A1 B1 sA1 sB1] = fit(siem(1:13), mill(1:13), w1_tot(1:13)) % w = dy.^(-2)

display("");

dy2_tot = sqrt(dsiem.^2+B2^2*dmill.^2);
w2_tot = dy1_tot.^(-2);
[A2 B2 sA2 sB2] = fit(siem(14:end), mill(14:end), w2_tot(14:end)) % w = dy.^(-2)

display("");

% chi 2
display("chi2");
chi_1 = chi2(siem(1:13), mill(1:13), dy1_tot(1:13), A1, B1)
display("");
chi_2 = chi2(siem(14:end), mill(14:end), dy2_tot(14:end), A2, B2)

% correggiamo
display("");display("correzione err per chi2");
sigma1 = sqrt(sum((siem(1:13) - A1 - B1.*mill(1:13)).^2) / (13-2))
sigma1 / dy1_tot(1)
%dy1_tot

display("");

sigma2 = sqrt(sum((siem(14:end) - A2 - B2.*mill(14:end)).^2) / (length(mill)-13-2))
sigma2 / dy1_tot(1)
%dy2_tot

% ritestiamo il chi2
display("");display("correzione chi2");
chi_1 = chi2(siem(1:13), mill(1:13), ones(13,1).*sigma1, A1, B1)
display("");
chi_2 = chi2(siem(14:end), mill(14:end), ones((length(mill)-13),1).*sigma2, A2, B2)