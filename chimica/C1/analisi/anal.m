clear Local user variables;

source("../../../algoritmi/alg1.m");
source("../../../algoritmi/utils.m");

mill = csvread("../dati/dati.csv")(2:(end), 1);
siem = csvread("../dati/dati.csv")(2:(end), 2);
dmill = ones(length(mill),1).*0.1/sqrt(12);
dsiem = ones(length(siem),1).*0.01/sqrt(12);

display("");

%[mill dmill siem dsiem]

fine = length(siem)

inizio_siem = siem(1:13);
inizio_mill = mill(1:13);

fine_siem = siem(14:fine);
fine_mill = mill(14:fine);

% fit preliminari
display("fit preliminari");
w = dsiem.^(-2);
inizio_w = w(1:13);
fine_w = w(14:fine);

[A1 B1 sA1 sB1] = fit(inizio_siem, inizio_mill, inizio_w) % w = dy.^(-2)
display("");
[A2 B2 sA2 sB2] = fit(fine_siem, fine_mill, fine_w) % w = dy.^(-2)

display("");display("");

% fit con incertezza x trasferita
display("fit secondari");
dy1_tot = sqrt(dsiem.^2+B1^2*dmill.^2);
w1_tot = dy1_tot.^(-2);
[A1 B1 sA1 sB1] = fit(inizio_siem, inizio_mill, w1_tot(1:13)) % w = dy.^(-2)

display("");

dy2_tot = sqrt(dsiem.^2+B2^2*dmill.^2);
w2_tot = dy1_tot.^(-2);
[A2 B2 sA2 sB2] = fit(fine_siem, fine_mill, w2_tot(14:fine)) % w = dy.^(-2)

display("");

% chi 2
display("chi2");
chi_1 = chi2(inizio_siem, inizio_mill, dy1_tot(1:13), A1, B1)
display("");
chi_2 = chi2(fine_siem, fine_mill, dy2_tot(14:fine), A2, B2)

% correggiamo
display("");display("correzione err per chi2");
sigma1 = sqrt(sum((inizio_siem - A1 - B1.*inizio_mill).^2) / (13-2))
sigma1 / dy1_tot(1)
%dy1_tot

display("");

sigma2 = sqrt(sum((fine_siem - A2 - B2.*fine_mill).^2) / (length(mill)-13-2))
sigma2 / dy1_tot(1) 
%dy2_tot

% ritestiamo il chi2
display("");display("correzione chi2");
chi_1 = chi2(inizio_siem, inizio_mill, ones(13,1).*sigma1, A1, B1)
display("");
chi_2 = chi2(fine_siem, fine_mill, ones((fine-13),1).*sigma2, A2, B2)

display("");
w1c_tot = sigma1.^(-2) * ones(13, 1);
w2c_tot = sigma2.^(-2) * ones(fine - 13, 1);
[q1 m1 sq1 sm1] = fit(inizio_siem, inizio_mill, w1c_tot) % w = dy.^(-2)
[q2 m2 sq2 sm2] = fit(fine_siem, fine_mill, w2c_tot) % w = dy.^(-2)

x = (q2 - q1) / (m1 - m2)
dx = sqrt(
    (sq2 / (m1 - m2))^2 +
    (sq1 / (m1 - m2))^2 +
    ((q2 - q1) / (m1 - m2)^2 * sm1)^2 +
    ((q2 - q1) / (m1 - m2)^2 * sm2)^2
)

mol_NaCl = x * 1.5e-3
dmol_NaCl = sqrt((dx * 1.5e-3)**2 + (x * 0.03e-3)**2)

c = mol_NaCl / 0.1
dc = sqrt((dmol_NaCl / 0.1)**2 + (mol_NaCl / 0.1**2 * 0.0003)**2)

qs = siem .^ 2;
w_qs = dsiem .^ -4;
[zero k2 szero sk2] = fit(qs(14:fine), fine_mill, w_qs(14:fine))
