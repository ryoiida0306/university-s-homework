hold on;

t = 1 : round(env_dim/2);
left_f = left_f(1:length(t));
right_f = right_f(1:length(t));
mean_X = mean(X);
mean_X = mean_X(1:length(t));
plot(t,left_f);
plot(t,right_f);
plot(t,mean_X);

my_plot_add

hold off;
