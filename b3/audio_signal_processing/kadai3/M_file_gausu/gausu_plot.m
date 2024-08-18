function [left_f,right_f] = gausu_plot(X)
    left_potential = 0.025;
    right_potential = 0.975;
    
    left_number = norminv(left_potential);
    right_number = norminv(right_potential);

    left_f = transpose(var(X)) * left_number + transpose(mean(X));
    right_f = transpose(var(X)) * right_number + transpose(mean(X));
end

