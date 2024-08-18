numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

for k = 1: numdata_test
 filename = sprintf('../test/u%d.wav', k);
 u_test_data = audioread(filename);
 c = fix(length(u_test_data)/2);
 u_test_cut = u_test_data(c-127: c+128);
 u_test_rceps = real(ifft(log(abs(fft(u_test_cut)))));
 u_test_cep = u_test_rceps(2:cep_dim);


 u2a_p = G(a_train_cep,X_u);
 u2i_p = G(i_train_cep,X_u);
 u2u_p = G(u_train_cep,X_u);
 u2e_p = G(e_train_cep,X_u);
 u2o_p = G(o_train_cep,X_u);

 max = u2a_p;
 if max < u2i_p, max = u2i_p; end;
 if max < u2u_p, max = u2u_p; end;
 if max < u2e_p, max = u2e_p; end;
 if max < u2o_p, max = u2o_p; end;

 if max == u2a_p, u_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif max == u2i_p, u_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif max == u2u_p, u_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif max == u2e_p, u_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif max == u2o_p, u_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
 end;
end;

disp('-------- u test results ---------')
count_a
count_i
count_u
count_e
count_o
correct_u = count_u
error_u = count_a + count_i + count_e + count_o
Acc_rate = (correct_u / numdata_test) * 100
