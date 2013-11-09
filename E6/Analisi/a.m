source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

Q = csvread("../Dati/flussi.csv")(:, 1);
dQ = csvread("../Dati/flussi.csv")(:, 2);

% percentuale errore
per_err = 0.1;

% ambiente...
T = 23 + 273;
dT = 1 / sqrt(12);

% viscosità aria a 23 °C
n = 1.85e-5;

% La nomenclatura fa cagare, lo so....
% leggiamo i dati
P1_L4 = csvread("../Dati/tubo_8000x4.csv")(:, 1);
dP1_L4 = P1_L4 .* per_err;
P2_L4 = csvread("../Dati/tubo_8000x4.csv")(:, 2);
dP2_L4 = P2_L4 .* per_err;

P1_C4 = csvread("../Dati/tubo_800x4.csv")(:, 1);
dP1_C4 = P1_C4 .* per_err;
P2_C4 = csvread("../Dati/tubo_800x4.csv")(:, 2);
dP2_C4 = P2_C4 .* per_err;

P1_L25 = csvread("../Dati/tubo_8000x2.5.csv")(:, 1);
dP1_L25 = P1_L25 .* per_err;
P2_L25 = csvread("../Dati/tubo_8000x2.5.csv")(:, 2);
dP2_L25 = P2_L25 .* per_err;

P1_C25 = csvread("../Dati/tubo_800x2.5.csv")(:, 1);
dP1_C25 = P1_C25 .* per_err;
P2_C25 = csvread("../Dati/tubo_800x2.5.csv")(:, 2);
dP2_C25 = P2_C25 .* per_err;

% ora abbiamo due dati per ciascun valore di flusso, mediamoli :-) neologismo
% è un po' un bordello, perché devo rovesciare l'ordine dei di metà sequenza di pressioni
P1_L4_m = mean([P1_L4(1:6)'; P1_L4(12:-1:7)'])';
dP1_L4_m = sqrt(dP1_L4(1:6)'.^2 .+ dP1_L4(12:-1:7)'.^2)';
P2_L4_m = mean([P2_L4(1:6)'; P2_L4(12:-1:7)'])';
dP2_L4_m = sqrt(dP2_L4(1:6)'.^2 .+ dP2_L4(12:-1:7)'.^2)';

P1_C4_m = mean([P1_C4(1:6)'; P1_C4(12:-1:7)'])';
dP1_C4_m = sqrt(dP1_C4(1:6)'.^2 .+ dP1_C4(12:-1:7)'.^2)';
P2_C4_m = mean([P2_C4(1:6)'; P2_C4(12:-1:7)'])';
dP2_C4_m = sqrt(dP2_C4(1:6)'.^2 .+ dP2_C4(12:-1:7)'.^2)';

P1_L25_m = mean([P1_L25(1:6)'; P1_L25(12:-1:7)'])';
dP1_L25_m = sqrt(dP1_L25(1:6)'.^2 .+ dP1_L25(12:-1:7)'.^2)';
P2_L25_m = mean([P2_L25(1:6)'; P2_L25(12:-1:7)'])';
dP2_L25_m = sqrt(dP2_L25(1:6)'.^2 .+ dP2_L25(12:-1:7)'.^2)';

P1_C25_m = mean([P1_C25(1:6)'; P1_C25(12:-1:7)'])';
dP1_C25_m = sqrt(dP1_C25(1:6)'.^2 .+ dP1_C25(12:-1:7)'.^2)';
P2_C25_m = mean([P2_C25(1:6)'; P2_C25(12:-1:7)'])';
dP2_C25_m = sqrt(dP2_C25(1:6)'.^2 .+ dP2_C25(12:-1:7)'.^2)';

% calcolo il delta pressione
DP_L4 = P2_L4_m .- P1_L4_m;
dDP_L4 = sqrt(dP1_L4_m .^ 2 .+ dP2_L4_m .^ 2);

DP_C4 = P2_C4_m .- P1_C4_m;
dDP_C4 = sqrt(dP1_C4_m .^ 2 .+ dP2_C4_m .^ 2);

DP_L25 = P2_L25_m .- P1_L25_m;
dDP_L25 = sqrt(dP1_L25_m .^ 2 .+ dP2_L25_m .^ 2);

DP_C25 = P2_C25_m .- P1_C25_m;
dDP_C25 = sqrt(dP1_C25_m .^ 2 .+ dP2_C25_m .^ 2);

% calcolo la pressione a metà tubo (interpolazione lineare)
P_L4 = P1_L4_m .+ DP_L4 ./ 2;
dP_L4 = sqrt(dP1_L4_m.^2 .+ dDP_L4.^2 / 4);

P_C4 = P1_C4_m .+ DP_C4 ./ 2;
dP_C4 = sqrt(dP1_C4_m.^2 .+ dDP_C4.^2 / 4);

P_L25 = P1_L25_m .+ DP_L25 ./ 2;
dP_L25 = sqrt(dP1_L25_m.^2 .+ dDP_L25.^2 / 4);

P_C25 = P1_C25_m .+ DP_C25 ./ 2;
dP_C25 = sqrt(dP1_C25_m.^2 .+ dDP_C25.^2 / 4);

% discriminante
j_L4 = P_L4(2:end) .* 0.004;
j_C4 = P_C4(2:end) .* 0.004;
j_L25 = P_L25(2:end) .* 0.0025;
j_C25 = P_C25(2:end) .* 0.0025;

% numero di Reynolds
k_4 = (4 * 0.029) / (pi * n * 0.004 * 8.314);
k_25 = (4 * 0.029) / (pi * n * 0.0025 * 8.314);
r_4 = k_4 * Q(5:end) / T;
dr_4 = sqrt((k_4 .* dQ(5:end) ./ T).^2 .+ (k_4 .* Q(5:end) * dT ./ T.^2).^2);
r_25 = k_25 * Q(5:end) / T;
dr_25 = sqrt((k_25 .* dQ(5:end) ./ T).^2 .+ (k_25 .* Q(5:end) * dT ./ T.^2).^2);

display("Reynolds 4");
display([r_4 dr_4]);

display("Reynolds 2.5");
display([r_25 dr_25]);

% conduttanze
C_L4 = Q(5:end) ./ DP_L4(2:end);
dC_L4 = sqrt((dQ(5:end) ./ DP_L4(2:end)).^2 .+ (Q(5:end) ./ (DP_L4(2:end).^2) .* dDP_L4(2:end)).^2);

C_C4 = Q(5:end) ./ DP_C4(2:end);
dC_C4 = sqrt((dQ(5:end) ./ DP_C4(2:end)).^2 .+ (Q(5:end) ./ (DP_C4(2:end).^2) .* dDP_C4(2:end)).^2);

C_L25 = Q(5:end) ./ DP_L25(2:end);
dC_L25 = sqrt((dQ(5:end) ./ DP_L25(2:end)).^2 .+ (Q(5:end) ./ (DP_L25(2:end).^2) .* dDP_L25(2:end)).^2);

C_C25 = Q(5:end) ./ DP_C25(2:end);
dC_C25 = sqrt((dQ(5:end) ./ DP_C25(2:end)).^2 .+ (Q(5:end) ./ (DP_C25(2:end).^2) .* dDP_C25(2:end)).^2);

% conduttanze teoriche
C_lam_L4 = 1350 .* P_L4(2:end) .* 0.004.^4 ./ 8;
C_lam_C4 = 1350 .* P_C4(2:end) .* 0.004.^4 ./ 0.8;
C_lam_L25 = 1350 .* P_L25(2:end) .* 0.0025.^4 ./ 8;
C_lam_C25 = 1350 .* P_C25(2:end) .* 0.0025.^4 ./ 0.8;

C_mol_L4 = 120 .* 0.004.^3 ./ 8
C_mol_C4 = 120 .* 0.004.^3 ./ 0.8
C_mol_L25 = 120 .* 0.0025.^3 ./ 8
C_mol_C25 = 120 .* 0.0025.^3 ./ 0.8

% empty line
display("");


% data printing
display("CONDUTTANZE");

display("Lungo 4");
display([C_L4, dC_L4, j_L4, C_lam_L4]);

display("Corto 4");
display([C_C4, dC_C4, j_C4, C_lam_C4]);

display("Lungo 2.5");
display([C_L25, dC_L25, j_L25, C_lam_L25]);

display("Corto 2.5");
display([C_C25, dC_C25, j_C25, C_lam_C25]);
