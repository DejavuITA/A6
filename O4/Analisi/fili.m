clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% tutte unità di misura in millimetri
er = 1;

% input dei dati
f5 = csvread("../Dati/fili.csv")(2:6, 1);
df5 = ones(length(f5), 1) .* er;

f10 = csvread("../Dati/fili.csv")(2:8, 2);
df10 = ones(length(f10), 1) .* er;

f20 = csvread("../Dati/fili.csv")(2:9, 3);
df20 = ones(length(f20), 1) .* er;

f40 = csvread("../Dati/fili.csv")(2:9, 4);
df40 = ones(length(f40), 1) .* er;

f80 = csvread("../Dati/fili.csv")(2:10, 5);
df80 = ones(length(f80), 1) .* er;

c = csvread("../Dati/fili.csv")(2:6, 6);
dc = ones(length(c), 1) .* er;

% lunghezze d'onda
red = 0.0006328;
orange = 0.000612;

% lunghezza 
l = 1555;
dl = 1;
% lunghezza storto
lst = 1565;
dlst = 1;

% angoli theta
t5 = (f5 ./ 2) ./ l;
dt5 = sqrt((df5./2./l).^2 .+ (f5./2./l.^2.*dl).^2);

t10 = (f10 ./ 2) ./ l;
dt10 = sqrt((df10./2./l).^2 .+ (f10./2./l.^2.*dl).^2);

t20 = (f20 ./ 2) ./ l;
dt20 = sqrt((df20./2./l).^2 .+ (f20./2./l.^2.*dl).^2);

t40 = (f40 ./ 2) ./ l;
dt40 = sqrt((df40./2./l).^2 .+ (f40./2./l.^2.*dl).^2);

t80 = (f80 ./ 2) ./ lst;
dt80 = sqrt((df80./2./lst).^2 .+ (f80./2./lst.^2.*dlst).^2);

tc = (c ./ 2) ./ l;
dtc = sqrt((dc./2./l).^2 .+ (c./2./l.^2.*dl).^2);

% dimensioni filo
s5 = (1:5)' .* red ./ t5
ds5 = ((1:5)' .* red ./ t5 .^ 2 .* dt5)

s10 = (1:7)' .* red ./ t10
ds10 = ((1:7)' .* red ./ t10 .^ 2 .* dt10)

s20 = (1:8)' .* red ./ t20
ds20 = ((1:8)' .* red ./ t20 .^ 2 .* dt20)

s40 = (1:8)' .* red ./ t40
ds40 = ((1:8)' .* red ./ t40 .^ 2 .* dt40)

s80 = (1:9)' .* red ./ t80
ds80 = ((1:9)' .* red ./ t80 .^ 2 .* dt80)

sc = (1:5)' .* red ./ tc
dsc = ((1:5)' .* red ./ tc .^ 2 .* dtc)

% media
m5 = weighted_mean(s5, ds5)
dm5= weighted_mean_err(ds5)

m10 = weighted_mean(s10, ds10)
dm10 = weighted_mean_err(ds10)

m20 = weighted_mean(s20, ds20)
dm20= weighted_mean_err(ds20)

m40 = weighted_mean(s40, ds40)
dm40 = weighted_mean_err(ds40)

m80 = weighted_mean(s80, ds80)
dm80= weighted_mean_err(ds80)

mc = weighted_mean(sc, dsc)
dmc = weighted_mean_err(dsc)