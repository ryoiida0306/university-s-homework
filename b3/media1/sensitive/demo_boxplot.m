%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings of plot in Matlab
% This code was written by Tatsuya Yokota (2020.03.26)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
close all;

%描画用関数，統計用関数を含むディレクトリを読み込む
addpath('plotting_function');
addpath('statistical_function');


%%%箱ひげ図%%%
distribution1 = randn(1000,1); %分布1, 正規分布, 標本数1000
distribution2 = 6*(rand(1500,1)-0.5); %分布2, 一様分布，標本数1500

X = {distribution1, distribution2}; % セル配列を定義

figure(1);clf;
myboxplot_x(X);
Yaxis_string(1:2,{'正規分布','一様分布'},12);%文字列を置く位置，置く文字列のセル，文字サイズ
grid on;
print('-dpng','example_boxplot_x.png');

figure(2);clf;
myboxplot_y(X);
Xaxis_string(1:2,{'正規分布','一様分布'},30,12);%文字列を置く位置，置く文字列のセル，文字サイズ
grid on;
print('-dpng','example_boxplot_y.png');



