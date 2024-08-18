X_a = zeros(0,cep_dim);
X_i = zeros(0,cep_dim);
X_u = zeros(0,cep_dim);
X_e = zeros(0,cep_dim);
X_o = zeros(0,cep_dim);



for k = 0 : 11
    my_number = k;
    train
    X_a = [X_a;transpose(a_train_cep)];
    X_i = [X_i;transpose(i_train_cep)];
    X_u = [X_u;transpose(u_train_cep)];
    X_e = [X_e;transpose(e_train_cep)];
    X_o = [X_o;transpose(o_train_cep)];
    
end

