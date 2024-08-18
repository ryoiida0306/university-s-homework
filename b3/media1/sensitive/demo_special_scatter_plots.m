%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings of plot in Matlab
% This code was written by Tatsuya Yokota (2020.03.27)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
close all;

addpath('plotting_function');
addpath('statistical_function');

%%% 第1第2主成分の係数を擬似的に生成
Z = randn(2,100);

%%% 100人の性別，年齢データをロード
load('parameters');

%%% クラスタープロットの作成
hf = figure(1);clf;hold on;
set(hf,'position',[0 0 800 800])

id1m = find(sex==1 & age < 20);
id2m = find(sex==1 & age >= 20 & age < 40);
id3m = find(sex==1 & age >= 40 & age < 60);
id4m = find(sex==1 & age >= 60 & age < 80);
id1f = find(sex==2 & age < 20);
id2f = find(sex==2 & age >= 20 & age < 40);
id3f = find(sex==2 & age >= 40 & age < 60);
id4f = find(sex==2 & age >= 60 & age < 80);

h(1)=plot(Z(1,id1m),Z(2,id1m),'bx','markersize',3);
h(2)=plot(Z(1,id2m),Z(2,id2m),'bx','markersize',5);
h(3)=plot(Z(1,id3m),Z(2,id3m),'bx','markersize',7);
h(4)=plot(Z(1,id4m),Z(2,id4m),'bx','markersize',9);
h(5)=plot(Z(1,id1f),Z(2,id1f),'ro','markersize',3);
h(6)=plot(Z(1,id2f),Z(2,id2f),'ro','markersize',5);
h(7)=plot(Z(1,id3f),Z(2,id3f),'ro','markersize',7);
h(8)=plot(Z(1,id4f),Z(2,id4f),'ro','markersize',9);

daspect([1 1 1])

xlabel('第1主成分(例)');
ylabel('第2主成分(例)');
legend(h,'Male, age < 20','Male, 20 <= age < 40','Male, 40 <= age < 60','Male, 60 <= age < 80','Female, age < 20','Female, 20 <= age < 40','Female, 40 <= age < 60','Female, 60 <= age < 80')
print('-dpng','example_scatter_plot_sex_age.png');


%%% 顔画像埋め込みプロットの作成
load('small_100faces.mat');%顔画像データのロード (64,64,3,100)

hf = figure(2);clf;hold on;
set(hf,'position',[0 0 800 800])
plot(Z(1,:),Z(2,:),'ko')
daspect([1 1 1])

ps = 0.1;
for id = 1:100

  pn  = Z(:,id) + 0.5*(rand(2,1)-0.5);
  hi = image([pn(1)-ps, pn(1)+ps ], [pn(2)-ps, pn(2)+ps],imgs(end:-1:1,end:-1:1,:,id));
  
end
xlabel('第1主成分(例)');
ylabel('第2主成分(例)');
print('-dpng','example_scatter_plot_face.png');

