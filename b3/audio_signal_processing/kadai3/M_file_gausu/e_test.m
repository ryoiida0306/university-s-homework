numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

for k = 1: numdata_test
 filename = sprintf('../test/e%d.wav', k);
 e_test_data = audioread(filename);
 c = fix(length(e_test_data)/2);
 e_test_cut = e_test_data(c-127: c+128);
 e_test_rceps = real(ifft(log(abs(fft(e_test_cut)))));
 e_test_cep = e_test_rceps(2:cep_dim);


 e2a_p = G(a_train_cep,X_e);
 e2i_p = G(i_train_cep,X_e);
 e2u_p = G(u_train_cep,X_e);
 e2e_p = G(e_train_cep,X_e);
 e2o_p = G(o_train_cep,X_e);

 max = e2a_p;
 if max < e2i_p, max = e2i_p; end;
 if max < e2u_p, max = e2u_p; end;
 if max < e2e_p, max = e2e_p; end;
 if max < e2o_p, max = e2o_p; end;

 if max == e2a_p, e_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif max == e2i_p, e_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif max == e2u_p, e_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif max == e2e_p, e_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif max == e2o_p, e_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
 end;
end;

disp('-------- e test results ---------')
count_a
count_i
count_u
count_e
count_o
correct_e = count_e
error_e = count_a + count_i + count_u + count_o
Acc_rate = (correct_e / numdata_test) * 100
