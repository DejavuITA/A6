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
tr100 = atan((r100 ./ 2) ./ l);
dtr100 = sqrt((dr100./2./l).^2 .+ (r100./2./l.^2.*dl).^2);
dtr100 = cos(tan(tr100)) ./ (1 + tr100.^2) .* dtr100;

tr300 = atan((r300 ./ 2) ./ l);
dtr300 = sqrt((dr300./2./l).^2 .+ (r300./2./l.^2.*dl).^2);
dtr300 = cos(tan(tr300)) ./ (1 + tr300.^2) .* dtr300;

tr600 = atan((r600 ./ 2) ./ l);
dtr600 = sqrt((dr600./2./l).^2 .+ (r600./2./l.^2.*dl).^2);
dtr600 = cos(tan(tr600)) ./ (1 + tr600.^2) .* dtr600;

to100 = atan((o100 ./ 2) ./ l);
dto100 = sqrt((do100./2./l).^2 .+ (o100./2./l.^2.*dl).^2);
dto100 = cos(tan(to100)) ./ (1 + to100.^2) .* dto100;

to300 = atan((o300 ./ 2) ./ l);
dto300 = sqrt((do300./2./l).^2 .+ (o300./2./l.^2.*dl).^2);
dto300 = cos(tan(to300)) ./ (1 + to300.^2) .* dto300;

to600 = atan((o600 ./ 2) ./ l);
dto600 = sqrt((do600./2./l).^2 .+ (o600./2./l.^2.*dl).^2);
dtro600 = cos(tan(to600)) ./ (1 + to600.^2) .* dto600;

% dimensioni fenditura
sr100 = (1:3)' .* red ./ sin(tr100)
dsr100 = ((1:3)' .* red ./ sin(tr100) .^ 2 .* cos(tr100) .* dtr100)

sr300 = (1:2)' .* red ./ sin(tr300)
dsr300 = ((1:2)' .* red ./ sin(tr300) .^ 2 .* cos(tr300)  .* dtr300)

sr600 = red ./ sin(tr600)
dsr600 = red ./ sin(tr600) .^ 2 .* cos(tr600)  .* dtr600

so100 = (1:3)' .* orange ./ sin(to100)
dso100 = ((1:3)' .* orange ./ sin(to100) .^ 2 .* cos(to100)  .* dto100)

so300 = (1:2)' .* orange ./ sin(to300)
dso300 = ((1:2)' .* orange ./ sin(to300) .^ 2 .* cos(to300)  .* dto300)

so600 = orange ./ sin(to600)
dso600 = orange ./ sin(to600) .^ 2 .* cos(to600)  .* dto600

% ora facciamo il rovescio, troviamo le lunghezze d'onda
% separazione tra fenditure
d1 = 100^-1;
d3 = 300^-1;
d6 = 600^-1;

lred1 = d1 .* sin(tr100) ./ (1:3)'
dlred1 = d1 .* cos(tr100) .* dtr100 ./ (1:3)'

lred3 = d3 .* sin(tr300) ./ (1:2)'
dlred3 = d3 .* cos(tr300) .* dtr300 ./ (1:2)'

lred6 = d6 .* sin(tr600)
dlred6 = d6 .* cos(tr600) .* dtr600


lorange1 = d1 .* sin(to100) ./ (1:3)'
dlorange1 = d1 .* cos(to100) .* dto100 ./ (1:3)'

lorange3 = d3 .* sin(to300) ./ (1:2)'
dlorange3 = d3 .* cos(to300) .* dto300 ./ (1:2)'

lorange6 = d6 .* sin(to600)
dlorange6 = d6 .* cos(to600) .* dto600

% ora facciamo le medie
% medie dimensioni fenditura
display("\n### FACCIAMO LE MEDIE ###################################");

display("Fenditure");

mr100 = weighted_mean(sr100, dsr100)
dmr100 = weighted_mean_err(dsr100)

statistic_mr100 = mean(sr100)
statistic_dmr100 = std(sr100)

mr300 = weighted_mean(sr300, dsr300)
dmr300 = weighted_mean_err(dsr300)

statistic_mr300 = mean(sr300)
statistic_dmr300 = std(sr300)

mr600 = weighted_mean(sr600, dsr600)
dmr600 = weighted_mean_err(dsr600)

statistic_mr600 = mean(sr600)
statistic_dmr600 = std(sr600)

display("");

mo100 = weighted_mean(so100, dso100)
dmo100 = weighted_mean_err(dso100)

statistic_mo100 = mean(so100)
statistic_dmo100 = std(so100)

mo300 = weighted_mean(so300, dso300)
dmo300 = weighted_mean_err(dso300)

statistic_mo300 = mean(so300)
statistic_dmo300 = std(so300)

mo600 = weighted_mean(so600, dso600)
dmo600 = weighted_mean_err(dso600)

statistic_mo600 = mean(so600)
statistic_dmo600 = std(so600)

display("\nLunghezze d'onda");

mlr100 = weighted_mean(lred1, dlred1)
dmlr100 = weighted_mean_err(dlred1)

statistic_mlr100 = mean(lred1)
statistic_dmlr100 = std(lred1)

mlr300 = weighted_mean(lred3, dlred3)
dmlr300 = weighted_mean_err(dlred3)

statistic_mlr300 = mean(lred3)
statistic_dmlr300 = std(lred3)

mlr600 = weighted_mean(lred6, dlred6)
dmlr600 = weighted_mean_err(dlred6)

statistic_mlr600 = mean(lred6)
statistic_dmlr600 = std(lred6)

display("");

mlo100 = weighted_mean(lorange1, dlorange1)
dmlo100 = weighted_mean_err(dlorange1)

statistic_mlo100 = mean(lorange1)
statistic_dmlo100 = std(lorange1)

mlo300 = weighted_mean(lorange3, dlorange3)
dmlo300 = weighted_mean_err(dlorange3)

statistic_mlo300 = mean(lorange3)
statistic_dmlo300 = std(lorange3)

mlo600 = weighted_mean(lorange6, dlorange6)
dmlo600 = weighted_mean_err(dlorange6)

statistic_mlo600 = mean(lorange6)
statistic_dmlo600 = std(lorange6)

display("\nValori definitivi mediati ulteriormente");

%fin_s100 = weighted_mean([mr100, mo100], [dmr100, dmo100])
%dfin_s100 = weighted_mean_err([dmr100, dmo100])
%
%weight_fin_s100 = weighted_mean([statistic_mr100, statistic_mo100],
	%[statistic_dmr100, statistic_dmo100])
%weight_dfin_s100 = weighted_mean_err([statistic_dmr100, statistic_dmo100])
%
%statistical_fin_s100 = mean([statistic_mr100, statistic_mo100])
%statistical_dfin_s100 = std([statistic_mr100, statistic_mo100])
%
%fin_s300 = weighted_mean([mr300, mo300], [dmr300, dmo300])
%dfin_s300 = weighted_mean_err([dmr300, dmo300])
%
%weight_fin_s300 = weighted_mean([statistic_mr300, statistic_mo300],
	%[statistic_dmr300, statistic_dmo300])
%weight_dfin_s300 = weighted_mean_err([statistic_dmr300, statistic_dmo300])
%
%statistical_fin_s300 = mean([statistic_mr300, statistic_mo300])
%statistical_dfin_s300 = std([statistic_mr300, statistic_mo300])
%
%fin_s600 = weighted_mean([mr600, mo600], [dmr600, dmo600])
%dfin_s600 = weighted_mean_err([dmr600, dmo600])

display("");

statistic_mro100 = mean([sr100; so100])
statistic_dmro100 = std([sr100; so100])

dens100 = 1/statistic_mro100
ddens100 = 1/(statistic_mro100.^2) * statistic_dmro100

statistic_mro300 = mean([sr300; so300])
statistic_dmro300 = std([sr300; so300])

dens300 = 1/statistic_mro300
ddens300 = 1/(statistic_mro300.^2) * statistic_dmro300

statistic_mro600 = mean([sr600; so600])
statistic_dmro600 = std([sr600; so600])

dens600 = 1/statistic_mro600
ddens600 = 1/(statistic_mro600.^2) * statistic_dmro600

###

w_mro100 = weighted_mean([sr100; so100], [dsr100; dso100])
w_dmro100 = weighted_mean_err([dsr100; dso100])

wdens100 = 1/w_mro100
wddens100 = 1/(w_mro100.^2) * w_dmro100

w_mro300 = weighted_mean([sr300; so300], [dsr300; dso300])
w_dmro300 = weighted_mean_err([dsr300; dso300])

wdens300 = 1/w_mro300
wddens300 = 1/(w_mro300.^2) * w_dmro300

w_mro600 = weighted_mean([sr600; so600], [dsr600; dso600])
w_dmro600 = weighted_mean_err([dsr600; dso600])

wdens600 = 1/w_mro600
wddens600 = 1/(w_mro600.^2) * w_dmro600

display("");

fin_lr = weighted_mean([mlr100, mlr300, mlr600],
	[dmlr100, dmlr300, dmlr600])
dfin_lr = weighted_mean_err([dmlr100, dmlr300, dmlr600])

weight_fin_lr = weighted_mean([statistic_mlr100, statistic_mlr300], [statistic_dmlr100, statistic_dmlr300])
weight_dfin_lr = weighted_mean_err([statistic_dmlr100, statistic_dmlr300])

statistical_fin_lr = mean([statistic_mlr100, statistic_mlr300, statistic_mlr600])
statistical_dfin_lr = std([statistic_mlr100, statistic_mlr300, statistic_mlr600])

fin_lo = weighted_mean([mlo100, mlo300, mlo600],
	[dmlo100, dmlo300, dmlo600])
dfin_lo = weighted_mean_err([dmlo100, dmlo300, dmlo600])

weight_fin_lo = weighted_mean([statistic_mlo100, statistic_mlo300], [statistic_dmlo100, statistic_dmlo300])
weight_dfin_lo = weighted_mean_err([statistic_dmlo100, statistic_dmlo300])

statistical_fin_lo = mean([statistic_mlo100, statistic_mlo300, statistic_mlo600])
statistical_dfin_lo = std([statistic_mlo100, statistic_mlo300, statistic_mlo600])

#culoculoculo