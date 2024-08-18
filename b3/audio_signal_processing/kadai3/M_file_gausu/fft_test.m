y = audioread(filename);
y_c = y(301:1324);
w = hamming(1024);
y_c_w = y_c .* w;
y_power = abs(fft(y_c_w));
y_spec = log(y_power);
y_cep = real(ifft(y_spec));
for k = n+1 : (length(y_cep)-n-1)
    y_cep(k) = 0;
end
y_env = real(fft(y_cep));







