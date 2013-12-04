clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% tutte unità di misura in millimetri
er = 1;

% input dei dati
c1i = csvread("../Dati/cerchio.csv")(2:end, 1);
c1e = csvread("../Dati/cerchio.csv")(2:end, 2);
dc1_ris = ones(length(c1i), 1) .* er;

c2i = csvread("../Dati/cerchio.csv")(2:end, 3);
c2e = csvread("../Dati/cerchio.csv")(2:end, 4);
dc2_ris = ones(length(c1i), 1) .* er;


% lunghezze d'onda
red = 0.0006328;
orange = 0.000612;

% lunghezza 
l = 1555;
dl = 1;
% lunghezza storto
lst = 1655;
dlst = 1;

% otteniamo il centro
c1 = mean([c1i, c1e]')';
dc1 = sqrt(sum(([c1i .- c1, c1e .- c1]').^2)' .+ dc1_ris.^2);

c2 = mean([c2i, c2e]')';
dc2 = sqrt(sum(([c2i .- c2, c2e .- c2]').^2)' .+ dc2_ris.^2);

% angoli theta
t1 = (c1 ./ 2) ./ l;
dt1 = sqrt((dc1./2./l).^2 .+ (c1./2./l.^2.*dl).^2);

t2 = (c2 ./ 2) ./ l;
dt2 = sqrt((dc2./2./l).^2 .+ (c2./2./l.^2.*dl).^2);

% dimensioni fenditura
s1 = 1.22 .* red ./ t1
ds1 = 1.22 .* red ./ t1 .^ 2 .* dt1

s2 = 1.22 .* red ./ t2
ds2 = 1.22 .* red ./ t2 .^ 2 .* dt2

% media
m1 = weighted_mean(s1, ds1)
dm1= weighted_mean_err(ds1)

m2 = weighted_mean(s2, ds2)
dm2 = weighted_mean_err(ds2)