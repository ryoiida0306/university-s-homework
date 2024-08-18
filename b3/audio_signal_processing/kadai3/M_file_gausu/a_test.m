numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

for k = 1: numdata_test
 filename = sprintf('../test/a%d.wav', k);
 a_test_data = audioread(filename);
 c = fix(length(a_test_data)/2);
 a_test_cut = a_test_data(c-127: c+128);
 a_test_rceps = real(ifft(log(abs(fft(a_test_cut)))));
 a_test_cep = a_test_rceps(2:cep_dim);




 a2a_p = G(a_train_cep,X_a);
 a2i_p = G(i_train_cep,X_a);
 a2u_p = G(u_train_cep,X_a);
 a2e_p = G(e_train_cep,X_a);
 a2o_p = G(o_train_cep,X_a);
 
 max = a2a_p;
 if max < a2i_p, max = a2i_p; end;
 if max < a2u_p, max = a2u_p; end;
 if max < a2e_p, max = a2e_p; end;
 if max < a2o_p, max = a2o_p; end;

 if max == a2a_p, a_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif max == a2i_p, a_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif max == a2u_p, a_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif max == a2e_p, a_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif max == a2o_p, a_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
 end;
end;

disp('-------- a test results ---------')
count_a
count_i
count_u
count_e
count_o
correct_a = count_a
error_a = count_i + count_u + count_e + count_o
Acc_rate = (correct_a / numdata_test) * 100
