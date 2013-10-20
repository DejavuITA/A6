# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/dati.csv");

ig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 76, 77, 78, 81];

# separa i dati
pompate = dati(ig .+ 1, 1);#(1:66,:); dati(2:end, 1)(67:end,:) .- 60];
pressioni = mmhg_to_pa(730 - dati(ig .+ 1, 2));
# sigma pressioni
s_pressioni = ones(length(pressioni), 1) * mmhg_to_pa(4.38/sqrt(6)); 

# risultati
best_b = 0;
best_A = 0;
best_sb = 0;
best_sA = 0;
best_chi = 0;
best_Pl = 0;
first = true;
for Pl=9000:11000,
    log_pressioni = log(pressioni .- Pl);
    s_log_pressioni = s_pressioni ./ pressioni;
    
    [b, A, sb, sA] = fit(log_pressioni, pompate, s_log_pressioni .^ -2);
    
    square_chi = chi2(log_pressioni, pompate, s_log_pressioni, b, A);
    
    if (first || square_chi < best_chi) && isreal(square_chi)
        best_chi = square_chi;
        best_A = A;
        best_b = b;
        best_sA = sA;
        best_sb = sb;
        best_Pl = Pl;
        
        first = false;
    end
end

# stampa risultati
A = best_A
sA = best_sA
b = best_b
sb = best_sb
B = Pl + exp(b)
sB = exp(b) * sb
chi = best_chi
Pl = best_Pl

log_pressioni = log(pressioni .- Pl);
s_log_pressioni = s_pressioni ./ pressioni;
contributions = chi2_contributions(log_pressioni, pompate, s_log_pressioni, b, A);

[(1:length(pressioni))', contributions]

indici_cannati = [67 68 69 70 71 72 73 74 75 79 80];