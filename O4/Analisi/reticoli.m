clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% tutte unità di misura in millimetri
er = 1;

% input dei dati
r100 = csvread("../Dati/reticolo.csv")(2:end, 1);
dr100 = ones(3, 1) .* er;

r300 = csvread("../Dati/reticolo.csv")(2:3, 2);
dr300 = ones(2, 1) .* er;

r600 = csvread("../Dati/reticolo.csv")(2, 3);
dr600 = er;

o100 = csvread("../Dati/reticolo.csv")(2:end, 4);
do100 = ones(3, 1) .* er;

o300 = csvread("../Dati/reticolo.csv")(2:3, 5);
do300 = ones(2, 1) .* er;

o600 = csvread("../Dati/reticolo.csv")(2, 6);
do600 = er;


% lunghezze d'onda
red = 0.0006328;
orange = 0.000612;

% lunghezza 
l = 1555;
dl = 1;
% lunghezza storto
lst = 1655;
dlst = 1;

% angoli theta
tr100 = (r100 ./ 2) ./ l;
dtr100 = sqrt((dr100./2./l).^2 .+ (r100./2./l.^2.*dl).^2);

tr300 = (r300 ./ 2) ./ l;
dtr300 = sqrt((dr300./2./l).^2 .+ (r300./2./l.^2.*dl).^2);

tr600 = (r600 ./ 2) ./ l;
dtr600 = sqrt((dr600./2./l).^2 .+ (r600./2./l.^2.*dl).^2);

to100 = (o100 ./ 2) ./ l;
dto100 = sqrt((do100./2./l).^2 .+ (o100./2./l.^2.*dl).^2);

to300 = (o300 ./ 2) ./ l;
dto300 = sqrt((do300./2./l).^2 .+ (o300./2./l.^2.*dl).^2);

to600 = (o600 ./ 2) ./ l;
dto600 = sqrt((do600./2./l).^2 .+ (o600./2./l.^2.*dl).^2);

% dimensioni fenditura
sr100 = (1:3)' .* red ./ tr100
dsr100 = ((1:3)' .* red ./ tr100 .^ 2 .* dtr100)

sr300 = (1:2)' .* red ./ tr300
dsr300 = ((1:2)' .* red ./ tr300 .^ 2 .* dtr300)

sr600 = red ./ tr600
dsr600 = red ./ tr600 .^ 2 .* dtr600

so100 = (1:3)' .* orange ./ tr100
dso100 = ((1:3)' .* orange ./ tr100 .^ 2 .* dtr100)

so300 = (1:2)' .* orange ./ tr300
dso300 = ((1:2)' .* orange ./ tr300 .^ 2 .* dtr300)

so600 = orange ./ tr600
dso600 = orange ./ tr600 .^ 2 .* dtr600

% ora facciamo il rovescio, troviamo le lunghezze d'onda
% separazione tra fenditure
d1 = 100^-1;
d3 = 300^-1;
d6 = 600^-1;

lred1 = d1 .* tr100 ./ (1:3)'
dlred1 = d1 .* dtr100 ./ (1:3)'

lred3 = d3 .* tr300 ./ (1:2)'
dlred3 = d3 .* dtr300 ./ (1:2)'

lred6 = d6 .* tr600
dlred6 = d6 .* dtr600


lorange1 = d1 .* to100 ./ (1:3)'
dlorange1 = d1 .* dto100 ./ (1:3)'

lorange3 = d3 .* to300 ./ (1:2)'
dlorange3 = d3 .* dto300 ./ (1:2)'

lorange6 = d6 .* to600
dlorange6 = d6 .* dto600

% ora facciamo le medie
% medie dimensioni fenditura
display("\n### FACCIAMO LE MEDIE ###################################");

mr100 = weighted_mean(sr100, dsr100)
dmr100 = weighted_mean_err(dsr100)

mr300 = weighted_mean(sr300, dsr300)
dmr300 = weighted_mean_err(dsr300)

mr600 = weighted_mean(sr600, dsr600)
dmr600 = weighted_mean_err(dsr600)


mo100 = weighted_mean(so100, dso100)
dmo100 = weighted_mean_err(dso100)

mo300 = weighted_mean(so300, dso300)
dmo300 = weighted_mean_err(dso300)

mo600 = weighted_mean(so600, dso600)
dmo600 = weighted_mean_err(dso600)


mlr100 = weighted_mean(lred1, dlred1)
dmlr100 = weighted_mean_err(dlred1)

mlr300 = weighted_mean(lred3, dlred3)
dmlr300 = weighted_mean_err(dlred3)

mlr600 = weighted_mean(lred6, dlred6)
dmlr600 = weighted_mean_err(dlred6)


mlo100 = weighted_mean(lorange1, dlorange1)
dmlo100 = weighted_mean_err(dlorange1)

mlo300 = weighted_mean(lorange3, dlorange3)
dmlo300 = weighted_mean_err(dlorange3)

mlo600 = weighted_mean(lorange6, dlorange6)
dmlo600 = weighted_mean_err(dlorange6)

#culoculoculo