# importa roba inutile di Dave
source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

# input dei dati
dati = csvread("../Dati/membrana.csv");

# separa i dati
tempo = dati(:, 1) .- 0.333;
pressioni = mmhg_to_pa(730 .- dati(:, 2) .* 2);
# sigma pressioni
s_pressioni = ones(length(pressioni), 1) * mmhg_to_pa(30/sqrt(12)); 

# risultati
best_b = 0;
best_A = 0;
best_sb = 0;
best_sA = 0;
best_chi = 0;
best_Pl = 0;
first = true;
for Pl=2000:4500,
    log_pressioni = log(pressioni .- Pl);
    s_log_pressioni = s_pressioni ./ pressioni;
    
    [b, A, sb, sA] = fit(log_pressioni, tempo, s_log_pressioni .^ -2);
    
    square_chi = chi2(log_pressioni, tempo, s_log_pressioni, b, A);
    
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