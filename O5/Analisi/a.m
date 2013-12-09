clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

L = csvread("../Dati/li.csv")(2:(end), 1);
i = csvread("../Dati/li.csv")(2:(end), 2);
i = i .- [0, 0, 0, 0, 0, 0, 0, 4.7, 4.7]';

function dc = err_c(c, dc)
	dv = 0.05;
	dc = sqrt((c .* dv) .^ 2 ./ 16 .+ \
		(c .* dv) .^ 2 ./ 64 .+ \
		dc .^ 2 ./ 4);
endfunction

dv = 0.05;
dc5 = err_c(1, 0)
dc25 = err_c(0.5, dc5)
dc125 = err_c(0.25, dc25)
dc0625 = err_c(0.125, dc125)

c = [1, 0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.5, 0.25, 0.125, 0.0625];
Ip = [7.4, 9.6, 13.3, 14.2, 17.2, 15.1, 17.3, 25.9, 49, 74, 91];
fs = [0, 0, 0, 0, 0, -4.7, -4.7, -4.7, -4.7, -4.7, -4.7];
I = Ip - fs;

dI = ones(1, length(I)) .* 1;
dlogI = dI ./ I;

[A, B, dA, dB] = fit(log(I), c, dlogI.^-2)

K = -B
a = exp(A)
da = exp(A) .* dA

di = ones(length(i), 1) .* 1;
dlogi = di ./ i;

[D, E, dD, dE] = fit(log(i), L, dlogi.^-2)

k = -E
d = exp(D)
dd = exp(D) .* dD 