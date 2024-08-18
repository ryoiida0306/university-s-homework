function p = G(in_vec,X)
    p = exp(-1/2*(transpose(in_vec-transpose(mean(X))) / cov(X) * (in_vec-transpose(mean(X)))))/(sqrt((2*pi).^(11))*det(cov(X)));
end