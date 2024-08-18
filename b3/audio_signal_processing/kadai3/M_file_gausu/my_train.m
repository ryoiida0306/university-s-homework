X = zeros(0,env_dim);
for datanum = 1 : 12
    filename = sprintf('../training/%s%02d.wav',boin,datanum);
    fft_test
    X = [X;transpose(y_env)];
end





    


