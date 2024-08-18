numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

for k = 1: numdata_test
 filename = sprintf('../test/o%d.wav', k);
 o_test_data = audioread(filename);
 c = fix(length(o_test_data)/2);
 o_test_cut = o_test_data(c-127: c+128);
 o_test_rceps = real(ifft(log(abs(fft(o_test_cut)))));
 o_test_cep = o_test_rceps(2:cep_dim);

 o2a_p = G(a_train_cep,X_o);
 o2i_p = G(i_train_cep,X_o);
 o2u_p = G(u_train_cep,X_o);
 o2e_p = G(e_train_cep,X_o);
 o2o_p = G(o_train_cep,X_o);

 max = o2a_p;
 if max < o2i_p, max = o2i_p; end;
 if max < o2u_p, max = o2u_p; end;
 if max < o2e_p, max = o2e_p; end;
 if max < o2o_p, max = o2o_p; end;

 if max == o2a_p, o_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif max == o2i_p, o_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif max == o2u_p, o_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif max == o2e_p, o_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif max == o2o_p, o_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
 end;
end;

disp('-------- o test results ---------')
count_a
count_i
count_u
count_e
count_o
correct_o = count_o
error_o = count_a + count_i + count_u + count_e
Acc_rate = (correct_o / numdata_test) * 100
