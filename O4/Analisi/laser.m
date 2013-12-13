clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% tutte unità di misura in millimetri
er = 1;

% input dei dati
f160 = csvread("../Dati/fenditura.csv")(2:(end), 1);
df160 = ones(length(f160), 1) .* er;

f80one = csvread("../Dati/fenditura.csv")(2:7, 2);
f80bis = csvread("../Dati/fenditura.csv")(2:7, 3);
df80_ris = ones(length(f80one), 1) .* er;

f40 = csvread("../Dati/fenditura.csv")(2:6, 4);
df40 = ones(length(f40), 1) .* er;

f20 = csvread("../Dati/fenditura.csv")(2:4, 5);
df20 = ones(length(f20), 1) .* er;

% lunghezze d'onda
red = 0.0006328;
orange = 0.000612;

% lunghezza 
l = 1555;
dl = 1;
% lunghezza storto
lst = 1655;
dlst = 1;

% mettiamo a posto l'80 che ha due serie
f80 = mean([f80one'; f80bis'])';
df80 = sqrt(sum(([f80one .- f80, f80bis .-f80]').^2)' .+ df80_ris.^2);

% angoli theta
t160 = (f160 ./ 2) ./ l;
dt160 = sqrt((df160./2./l).^2 .+ (f160./2./l.^2.*dl).^2);

t80 = (f80 ./ 2) ./ l;
dt80 = sqrt((df80./2./l).^2 .+ (f80./2./l.^2.*dl).^2);

t40 = (f40 ./ 2) ./ l;
dt40 = sqrt((df40./2./l).^2 .+ (f40./2./l.^2.*dl).^2);

t20 = (f20 ./ 2) ./ l;
dt20 = sqrt((df20./2./l).^2 .+ (f20./2./l.^2.*dl).^2);

% dimensioni fenditura
s160 = (1:10)' .* red ./ t160;
ds160 = ((1:10)' .* red ./ t160 .^ 2 .* dt160);
ms160 = [s160, ds160]

s80 = (1:6)' .* red ./ t80;
ds80 = ((1:6)' .* red ./ t80 .^ 2 .* dt80);
ms80 = [s80, ds80]

s40 = (1:5)' .* red ./ t40;
ds40 = ((1:5)' .* red ./ t40 .^ 2 .* dt40);
ms40 = [s40, ds40]

s20 = (1:3)' .* red ./ t20;
ds20 = ((1:3)' .* red ./ t20 .^ 2 .* dt20);
ms20 = [s20, ds20]

% media
m160 = weighted_mean(s160, ds160);
dm160 = weighted_mean_err(ds160);
statistic_dm160 = std(s160);
mm160 = [m160, dm160, statistic_dm160]

m80 = weighted_mean(s80, ds80);
dm80 = weighted_mean_err(ds80);
statistic_dm80 = std(s80);
mm80 = [m80, dm80, statistic_dm80]

m40 = weighted_mean(s40, ds40);
dm40 = weighted_mean_err(ds40);
statistic_dm40 = std(s40);
mm40 = [m40, dm40, statistic_dm40]

m20 = weighted_mean(s20, ds20);
dm20 = weighted_mean_err(ds20);
statistic_dm20 = std(s20);
mm20 = [m20, dm20, statistic_dm20]