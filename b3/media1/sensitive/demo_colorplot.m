%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings of plot in Matlab
% This code was written by Tatsuya Yokota (2020.03.26)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
close all;

%描画用関数，統計用関数を含むディレクトリを読み込む
addpath('plotting_function');
addpath('statistical_function');

%%%色プロット%%%
x_names = {'ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI'};
y_names = {'あいう', 'いうえ', 'うえお' ,'えおか', 'おかき'};

R = rand(5,7);

figure(1);clf;
imagesc(R);
colorbar;caxis([0 1]);
Xaxis_string(1:7,x_names,30,12);%文字列を置く位置，置く文字列のセル，角度，文字サイズ
Yaxis_string(1:5,y_names,12);%文字列を置く位置，置く文字列のセル，文字サイズ
print('-dpng','example_colorplot.png');

