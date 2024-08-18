numdata_test = 6;
count_a = 0;
count_i = 0;
count_u = 0;
count_e = 0;
count_o = 0;

a2a_dist = 0;
a2i_dist = 0;
a2u_dist = 0;
a2e_dist = 0;
a2o_dist = 0;


for k = 1: numdata_test
 filename = sprintf('../test/a%d.wav', k);
 a_test_data = audioread(filename);
 c = fix(length(a_test_data)/2);
 a_test_cut = a_test_data(c-127: c+128);
 a_test_rceps = real(ifft(log(abs(fft(a_test_cut)))));
 a_test_cep = a_test_rceps(2:cep_dim);
 
 for my_number = 0 : 11
    train
    a2a_dist = a2a_dist + norm(a_train_cep - a_test_cep);
    a2i_dist = a2i_dist + norm(i_train_cep - a_test_cep);
    a2u_dist = a2u_dist + norm(u_train_cep - a_test_cep);
    a2e_dist = a2e_dist + norm(e_train_cep - a_test_cep);
    a2o_dist = a2o_dist + norm(o_train_cep - a_test_cep);
 end;

 min = a2a_dist;
 if min > a2i_dist, min = a2i_dist; end;
 if min > a2u_dist, min = a2u_dist; end;
 if min > a2e_dist, min = a2e_dist; end;
 if min > a2o_dist, min = a2o_dist; end;

 if min == a2a_dist, a_answer = sprintf('%s\n', 'a'); count_a = count_a + 1;
 elseif min == a2i_dist, a_answer = sprintf('%s\n', 'i'); count_i = count_i + 1;
 elseif min == a2u_dist, a_answer = sprintf('%s\n', 'u'); count_u = count_u + 1;
 elseif min == a2e_dist, a_answer = sprintf('%s\n', 'e'); count_e = count_e + 1;
 elseif min == a2o_dist, a_answer = sprintf('%s\n', 'o'); count_o = count_o + 1;
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
