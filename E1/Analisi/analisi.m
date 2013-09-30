# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/dati.csv");

# separa i dati
pompate = dati(2:end, 1);#(1:66,:); dati(2:end, 1)(67:end,:) .- 60];
pressioni = mmhg_to_pa(730 - dati(2:end, 2));
# sigma pressioni
s_pressioni = ones(length(pressioni), 1) * mmhg_to_pa(1/sqrt(6)); 

# risultati
best_b = 0;
best_A = 0;
best_sb = 0;
best_sA = 0;
best_chi = 0;
best_Pl = 0;
first = true;
for Pl=8000:12000,
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
B = exp(b)
sB = exp(b) * sb
chi = best_chi
Pl = best_Pl

log_pressioni = log(pressioni .- Pl);
s_log_pressioni = s_pressioni ./ pressioni;
contributions = chi2_contributions(log_pressioni, pompate, s_log_pressioni, b, A);

[(1:length(pressioni))', contributions]

indici_cannati = [67 68 69 70 71 72 73 74 75 79 80];

chi = sum(contributions) - sum(contributions([indici_cannati]))