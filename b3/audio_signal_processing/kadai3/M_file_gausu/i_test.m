numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

for k = 1: numdata_test
 filename = sprintf('../test/i%d.wav', k);
 i_test_data = audioread(filename);
 c = fix(length(i_test_data)/2);
 i_test_cut = i_test_data(c-127: c+128);
 i_test_rceps = real(ifft(log(abs(fft(i_test_cut)))));
 i_test_cep = i_test_rceps(2:cep_dim);

 
 i2a_p = G(a_train_cep,X_i);
 i2i_p = G(i_train_cep,X_i);
 i2u_p = G(u_train_cep,X_i);
 i2e_p = G(e_train_cep,X_i);
 i2o_p = G(o_train_cep,X_i);
 

 max = i2a_p;
 if max < i2i_p, max = i2i_p; end;
 if max < i2u_p, max = i2u_p; end;
 if max < i2e_p, max = i2e_p; end;
 if max < i2o_p, max = i2o_p; end;

 if max == i2a_p, i_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif max == i2i_p, i_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif max == i2u_p, i_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif max == i2e_p, i_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif max == i2o_p, i_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
 end;
end;

disp('-------- i test results ---------')
count_a
count_i
count_u
count_e
count_o
correct_i = count_i
error_i = count_a + count_u + count_e + count_o
Acc_rate = (correct_i / numdata_test) * 100
