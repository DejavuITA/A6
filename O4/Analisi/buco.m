clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

% tutte unità di misura in millimetri
er = 0.5;

% input dei dati
c1i = csvread("../Dati/cerchio.csv")(2:end, 1);
dc1i = ones(length(c1i), 1) .* er;

c1e = csvread("../Dati/cerchio.csv")(2:end, 2);
dc1e = ones(length(c1i), 1) .* er;

c2i = csvread("../Dati/cerchio.csv")(2:end, 3);
dc2i = ones(length(c1i), 1) .* er;

c2e = csvread("../Dati/cerchio.csv")(2:end, 4);
dc2e = ones(length(c1i), 1) .* er;

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
t5 = (f5 ./ 2) ./ l;
dt5 = sqrt((df5./2./l).^2 .+ (f5./2./l.^2).^2);

t10 = (f10 ./ 2) ./ l;
dt10 = sqrt((df10./2./l).^2 .+ (f10./2./l.^2).^2);

t20 = (f20 ./ 2) ./ l;
dt20 = sqrt((df20./2./l).^2 .+ (f20./2./l.^2).^2);

t40 = (f40 ./ 2) ./ l;
dt40 = sqrt((df40./2./l).^2 .+ (f40./2./l.^2).^2);

t80 = (f80 ./ 2) ./ l;
dt80 = sqrt((df80./2./l).^2 .+ (f80./2./l.^2).^2);

tc = (c ./ 2) ./ l;
dtc = sqrt((dc./2./l).^2 .+ (c./2./l.^2).^2);

% dimensioni fenditura
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