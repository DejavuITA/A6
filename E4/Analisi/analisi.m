# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
V = 5930 * 10^(-6);
dV = 10 * 10^(-6);
err = 0.1;
P_atm = 98100;
dP_atm = 100 / sqrt(12);
Deg = csvread("../Dati/csv/deg.csv")(1:end, 1:2);
dDeg = err .* Deg(:,2) .* 100; % Deg(1,2) .* ones(length(Deg),1) .* err; 
Giro1 = csvread("../Dati/csv/giro1.csv")(1:end, 1:2);
dGiro1 = err .* Giro1(:,2) .* 100;
Giro2 = csvread("../Dati/csv/giro2.csv")(1:end, 1:2);
dGiro2 = err .* Giro2(:,2) .* 100;
Giro3 = csvread("../Dati/csv/giro3.csv")(1:end, 1:2);
dGiro3 = err .* Giro3(:,2) .* 100;
Giro4 = csvread("../Dati/csv/giro4.csv")(1:end, 1:2);
dGiro4 = err .* Giro4(:,2) .* 100;
Giro50 = csvread("../Dati/csv/giro5.0.csv")(1:end, 1:2);
dGiro50 = err .* Giro50(:,2) .* 100;
Giro52 = csvread("../Dati/csv/giro5.2.csv")(1:end, 1:2);
dGiro52 = err .* Giro52(:,2) .* 100;
Giro54 = csvread("../Dati/csv/giro5.4.csv")(1:end, 1:2);
dGiro54 = err .* Giro54(:,2) .* 100;
Giro56 = csvread("../Dati/csv/giro5.6.csv")(1:end, 1:2);
dGiro56 = err .* Giro56(:,2) .* 100;
Giro58 = csvread("../Dati/csv/giro5.8.csv")(1:end, 1:2);
dGiro58 = err .* Giro58(:,2) .* 100;
Giro6 = csvread("../Dati/csv/giro6.csv")(1:end, 1:2);
dGiro6 = err .* Giro6(:,2) .* 100;
Giro7 = csvread("../Dati/csv/giro7.csv")(1:end, 1:2);
dGiro7 = err .* Giro7(:,2) .* 100;
Giro8 = csvread("../Dati/csv/giro8.csv")(1:end, 1:2);
dGiro8 = err .* Giro8(:,2) .* 100;
Giro9 = csvread("../Dati/csv/giro9.csv")(1:end, 1:2);
dGiro9 = err .* Giro9(:,2) .* 100;

er = 0.001;

# fit delle rette
% function A, B, sA, sB = fit(y, x, w) % w = dy^(-2)
y = Deg(:,2) .* 100;
x = Deg(:,1) .- 1237; %x = Deg(:,1);
w = dDeg.^-2;
#w = er * ones(length(Deg), 1);
[Ag Bg sAg sBg] = fit( y, x, w);
[Bg sBg];
chi_g = chi2(y, x, w, Ag, Bg);
#errorbar(x, y, dDeg, "o")

y = Giro1(:,2) .* 100;
x = Giro1(:,1) - Giro1(1,1);
w = dGiro1.^-2;
#w = er * ones(length(Giro1), 1);
[A1 B1 sA1 sB1] = fit( y, x, w);
[B1 sB1];
chi_1 = chi2(y, x, w, A1, B1);

y = Giro2(:,2) .* 100;
x = Giro2(:,1) - Giro2(1,1);
w = dGiro2.^-2;
#w = er * ones(length(Giro2), 1);
[A2 B2 sA2 sB2] = fit(y, x, w);
[B2 sB2];
chi_2 = chi2(y, x, w, A2, B2);

y = Giro3(:,2) .* 100;
x = Giro3(:,1) - Giro3(1,1);
w = dGiro3.^-2;
#w = er * ones(length(Giro3), 1);
[A3 B3 sA3 sB3] = fit( y, x, w);
[B3 sB3];
chi_3 = chi2(y, x, w, A3, B3);

y = Giro4(:,2) .* 100;
x = Giro4(:,1) - Giro4(1,1);
w = dGiro4.^-2;
#w = er * ones(length(Giro4), 1);
[A4 B4 sA4 sB4] = fit( y, x, w);
[B4 sB4];
chi_4 = chi2(y, x, w, A4, B4);

y = Giro50(:,2) .* 100;
x = Giro50(:,1) - Giro50(1,1);
w = dGiro50.^-2;
#w = er * ones(length(Giro50), 1);
[A50 B50 sA50 sB50] = fit( y, x, w);
[B50 sB50];
chi_50 = chi2(y, x, w, A50, B50);

y = Giro52(:,2) .* 100;
x = Giro52(:,1) - Giro52(1,1);
w = dGiro52.^-2;
#w = er * ones(length(Giro52), 1);
[A52 B52 sA52 sB52] = fit( y, x, w);
[B52 sB52];
chi_52 = chi2(y, x, w, A52, B52);

y = Giro54(:,2) .* 100;
x = Giro54(:,1) - Giro54(1,1);
w = dGiro54.^-2;
#w = er * ones(length(Giro54), 1);
[A54 B54 sA54 sB54] = fit( y, x, w);
[B54 sB54];
chi_54 = chi2(y, x, w, A54, B54);

y = Giro56(:,2) .* 100;
x = Giro56(:,1) - Giro56(1,1);
w = dGiro56.^-2;
#w = er * ones(length(Giro56), 1);
[A56 B56 sA56 sB56] = fit( y, x, w);
[B56 sB56];
chi_56 = chi2(y, x, w, A56, B56);

y = Giro58(:,2) .* 100;
x = Giro58(:,1) - Giro58(1,1);
w = dGiro58.^-2;
#w = er * ones(length(Giro58), 1);
[A58 B58 sA58 sB58] = fit( y, x, w);
[B58 sB58];
chi_58 = chi2(y, x, w, A58, B58);

y = Giro6(:,2) .* 100;
x = Giro6(:,1) - Giro6(1,1);
w = dGiro6.^-2;
#w = ones(length(Giro6), 1);
[A6 B6 sA6 sB6] = fit( y, x, w);
[B6 sB6];
chi_6 = chi2(y, x, w, A6, B6);

y = Giro7(:,2) .* 100;
x = Giro7(:,1) - Giro7(1,1);
w = dGiro7.^-2;
#w = er * ones(length(Giro7), 1);
[A7 B7 sA7 sB7] = fit( y, x, w);
[B7 sB7];
chi_7 = chi2(y, x, w, A7, B7);

y = Giro8(:,2) .* 100;
x = Giro8(:,1) - Giro8(1,1);
w = dGiro8.^-2;
#w = er * ones(length(Giro8), 1);
[A8 B8 sA8 sB8] = fit( y, x, w);
[B8 sB8];
chi_8 = chi2(y, x, w, A8, B8);

y = Giro9(:,2) .* 100;
x = Giro9(:,1) - Giro9(1,1);
w = dGiro9.^-2;
#w = er * ones(length(Giro9), 1);
[A9 B9 sA9 sB9] = fit( y, x, w);
[B9 sB9];
chi_9 = chi2(y, x, w, A9, B9);

giri = [1; 2; 3; 4; 5; 5.2; 5.4; 5.6; 5.8; 6; 7; 8; 9];
A = [A1; A2; A3; A4; A50; A52; A54; A56; A58; A6; A7; A8; A9];
B = [B1; B2; B3; B4; B50; B52; B54; B56; B58; B6; B7; B8; B9];
dB = [sB1; sB2; sB3; sB4; sB50; sB52; sB54; sB56; sB58; sB6; sB7; sB8; sB9];
Q = V .* (B .- Bg);
dQ = sqrt(V.^2 .* (dB .^2 .+ sBg.^2) .+ (B .- Bg).^2 .* (dV^2));
[Q dQ]
%errorbar(giri, Q, dQ, "~")

Qg = V .* Bg
dQg = sqrt(V.^2 * sBg ^2 + Bg^2 * dV ^ 2)

vP = P_atm .- [mean(Giro1(:, 2)), mean(Giro2(:, 2)), mean(Giro3(:, 2)),   mean(Giro4(:, 2)), mean(Giro50(:, 2)), mean(Giro52(:, 2)),   mean(Giro54(:, 2)), mean(Giro56(:, 2)), mean(Giro58(:, 2)),    mean(Giro6(:, 2)), mean(Giro7(:, 2)), mean(Giro8(:, 2)), mean(Giro9(:, 2))]';
C = Q ./ P_atm;
dC = sqrt((dQ ./ P_atm) .^ 2 + (Q * dP_atm ./ (P_atm .^ 2)) .^ 2);
[C dC]

vm = sqrt(8 * 8.3144 * 293 / (pi * 0.029));
d = (C .* 12 .* 0.08 / (pi * vm)) .^ (1/3);

[
chi_g, length(Deg) - 2; %length(Deg) - 2;
chi_1, length(Giro1) - 2;
chi_2, length(Giro2) - 2;
chi_3, length(Giro3) - 2;
chi_4, length(Giro4) - 2;
chi_50, length(Giro50) - 2;
chi_52, length(Giro52) - 2;
chi_54, length(Giro54) - 2;
chi_56, length(Giro56) - 2;
chi_58, length(Giro58) - 2;
chi_6, length(Giro6) - 2;
chi_7, length(Giro7) - 2;
chi_8, length(Giro8) - 2;
chi_9, length(Giro9) - 2;
]

#dDeg = err .* Deg(:,2)
#dGiro1 = err .* Giro1(:,2)
#dGiro2 = err .* Giro2(:,2)
#dGiro3 = err .* Giro3(:,2)
#dGiro4 = err .* Giro4(:,2)
#dGiro50 = err .* Giro50(:,2)
#dGiro52 = err .* Giro52(:,2)
#dGiro54 = err .* Giro54(:,2)
#dGiro56 = err .* Giro56(:,2)
#dGiro58 = err .* Giro58(:,2)
#dGiro6 = err .* Giro6(:,2)
#dGiro7 = err .* Giro7(:,2)
#dGiro8 = err .* Giro8(:,2)
#dGiro9 = err .* Giro9(:,2)
