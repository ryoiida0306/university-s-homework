clear all;
close all;

load('parameters.mat');
addpath('plotting_function');
addpath('statistical_function');
load("week2_data_2022A.mat")
load('small_100faces.mat');%顔画像データのロード (64,64,3,100)


%課題1
%{

sex1 = zeros(1,47);
sex2 = zeros(1,53);

%sex1,sex2配列を作る
sex1length = 1;
sex2length = 1;
for i = 1:length(sex)
    if sex(i) == 1
        sex1(sex1length) = age(i);
        sex1length = sex1length+1;
    else
        sex2(sex2length) = age(i);
        sex2length = sex2length+1;
    end
end

%ヒストグラムプロット
figure
subplot(1,2,1)
histogram(sex1,10)
title("男性の年齢別ヒストグラム")
xlabel("年齢")
ylabel("人数")
subplot(1,2,2)
histogram(sex2,10)
title("女性の年齢別ヒストグラム")
xlabel("年齢")
ylabel("人数")
print('-dpng','exp1_hist.png');

%性別による平均年齢に有意差があるのかt検定
E1 = mean(sex1);
E2 = mean(sex2);
V1 = var(sex1,0);
V2 =var(sex2,0);
N1 = length(sex1);
N2 = length(sex2);
s = sqrt(((N1-1)*V1+(N2-1)*V2)/(N1+N2-2));
t = (E1-E2)/s*sqrt(1/N1+1/N2);
v = N1+N2-2;
p = 2*tcdf(-abs(t),v);
if p<0.01
    disp("有意性あり（p<0.01）")
else
    if p<0.05
        disp("有意性あり(p<0.05)")
    else 
        disp("有意性があるとは言えない")
    end
end
disp(p)
figure
subplot(2,1,1)
myboxplot_x(sex1)
xlabel("年齢")
ylabel("男性")
title("男女別箱ひげ図")
subplot(2,1,2)
myboxplot_x(sex2)
xlabel("年齢")
ylabel("女性")
print('-dpng','exp1_boxplot.png');

%}
%課題2



load("week2_data_2022A.mat")



Sr=corrcoef([sex,Y]);
Ar=corrcoef([age,Y]);

Sr = Sr(2:11);
Ar = Ar(2:11);
R = zeros(2,10);
R(1,:) = Sr;
R(2,:) = Ar;
disp(R)

figure
y_names = {'冷たい', '利他的な', '頑固な', '嫌い', '支配的な', '下品な', '強い', '理性的な', '陰気な', '消極的な'};
x_names = {'性別', '年齢'};

imagesc(transpose(R));
colorbar;caxis([-1 1]);
Xaxis_string(1:2,x_names,30,12);%文字列を置く位置，置く文字列のセル，角度，文字サイズ
Yaxis_string(1:10,y_names,12);%文字列を置く位置，置く文字列のセル，文字サイズ
title("印象データvs性別,年齢の相関係数カラーマップ表示")
print('-dpng','exp1_cor.png');

%課題3
%{



S = cov(Y);
figure
imagesc(S);
colorbar;caxis([-1 1]);
title("印象データ10項目に関する分散共分散行列")
strImp = {'冷たい', '利他的な', '頑固な', '嫌い', '支配的な', '下品な', '強い', '理性的な', '陰気な', '消極的な'};
xticklabels(strImp)
yticklabels(strImp)
print('-dpng','cov_matrix.png');
[V,D]=svd(S);

figV = V(:,(1:4));%第一～第四主成分の行列
disp(figV)
figD = transpose(diag(D));
figD = figD(1:4);%第一から第四固有値の行列
disp(figD)

%寄与率、累積寄与率を求める
lamda = diag(D);
lamSum = sum(lamda);
Con = lamda/lamSum;
AcCon = zeros(1,length(D));
for i = 1:length(D)
    for j = 1:i
        AcCon(i) = AcCon(i)+Con(j);
    end
end
figCon = transpose(Con);
figCon = figCon(1:4);

figAcCon = AcCon(1:4);
disp(figCon)
disp(figAcCon)
%主成分分析による散布図
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Settings of plot in Matlab
% This code was written by Tatsuya Yokota (2020.03.27)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

addpath('plotting_function');
addpath('statistical_function');

%%% 第1第2主成分の係数を擬似的に生成

Z = Y*V(:,(1:2));
Z = transpose(Z);

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

h(1)=plot(Z(1,id1m),Z(2,id1m),'bx','markersize',5);
h(2)=plot(Z(1,id2m),Z(2,id2m),'bx','markersize',7);
h(3)=plot(Z(1,id3m),Z(2,id3m),'bx','markersize',9);
h(4)=plot(Z(1,id4m),Z(2,id4m),'bx','markersize',11);
h(5)=plot(Z(1,id1f),Z(2,id1f),'ro','markersize',5);
h(6)=plot(Z(1,id2f),Z(2,id2f),'ro','markersize',7);
h(7)=plot(Z(1,id3f),Z(2,id3f),'ro','markersize',9);
h(8)=plot(Z(1,id4f),Z(2,id4f),'ro','markersize',11);

daspect([1 1 1])

xlabel('第1主成分',fontsize = 18);
ylabel('第2主成分',fontsize = 18);
legend(h,'Male, age < 20','Male, 20 <= age < 40','Male, 40 <= age < 60','Male, 60 <= age < 80','Female, age < 20','Female, 20 <= age < 40','Female, 40 <= age < 60','Female, 60 <= age < 80',fontsize = 15)
print('-dpng','face_pca_1.png');


%%% 顔画像埋め込みプロットの作成
load('small_100faces.mat');%顔画像データのロード (64,64,3,100)

hf = figure(2);clf;hold on;
set(hf,'position',[0 0 800 800])
plot(Z(1,:),Z(2,:),'ko')
daspect([1 1 1])

ps = 0.3;
for i = 1:100

  pn  = Z(:,i) + 0.5*(rand(2,1)-0.5);
  hi = image([pn(1)-ps, pn(1)+ps ], [pn(2)-ps, pn(2)+ps],imgs(end:-1:1,end:-1:1,:,i));
end
xlabel('第1主成分',fontsize = 18);
ylabel('第2主成分',fontsize = 18);
print('-dpng','face_pca_2.png');
%}
%課題4
%{

S = cov(Y);
[V,D]=svd(S);

Z = Y*V(:,(1:2));
Z = transpose(Z);

hold off
hf = figure(1);clf;hold on;
set(hf,'position',[0 0 800 800])

candidates_sex = zeros(length(ID),1);
candidates_age = zeros(length(ID),1);


for i = 1:length(ID)
    tmpsex = sex(ID(i));
    tmpage = age(ID(i));
    candidates_sex(i) = tmpsex;
    candidates_age(i) = tmpage;
end

sex = candidates_sex;
age = candidates_age;

id1m = ID(find(sex==1 & age < 20));
id2m = ID(find(sex==1 & age >= 20 & age < 40));
id3m = ID(find(sex==1 & age >= 40 & age < 60));
id4m = ID(find(sex==1 & age >= 60 & age < 80));
id1f = ID(find(sex==2 & age < 20));
id2f = ID(find(sex==2 & age >= 20 & age < 40));
id3f = ID(find(sex==2 & age >= 40 & age < 60));
id4f = ID(find(sex==2 & age >= 60 & age < 80));

%h(1)=plot(Z(1,id1m),Z(2,id1m),'bx','markersize',3);
%h(2)=plot(Z(1,id2m),Z(2,id2m),'bx','markersize',5);
h(3)=plot(Z(1,id3m),Z(2,id3m),'bx','markersize',7);
h(4)=plot(Z(1,id4m),Z(2,id4m),'bx','markersize',9);
%h(5)=plot(Z(1,id1f),Z(2,id1f),'ro','markersize',3);
%h(6)=plot(Z(1,id2f),Z(2,id2f),'ro','markersize',5);
h(7)=plot(Z(1,id3f),Z(2,id3f),'ro','markersize',7);
%h(8)=plot(Z(1,id4f),Z(2,id4f),'ro','markersize',9);

%顔画像プロット

hf = figure(2);clf;hold on;
set(hf,'position',[0 0 800 800])
plot(Z(1,ID),Z(2,ID),'ko')
daspect([1 1 1])

ps = 0.3;
for i = 1:length(ID)

  pn  = Z(:,ID(i)) + 0.5*(rand(2,1)-0.5);
  hi = image([pn(1)-ps, pn(1)+ps ], [pn(2)-ps, pn(2)+ps],imgs(end:-1:1,end:-1:1,:,ID(i)));
  
end
text(Z(1,ID),Z(2,ID),num2str(T),Color=[1,0,1],fontsize = 18)
xlabel('第1主成分',fontsize = 18);
ylabel('第2主成分',fontsize = 18);
print('-dpng','election_pca.png');
%}
%課題5
%{
subY=Y(ID,:);

S=cov(subY);

[V,D]=svd(subY);

Z = subY*V(:,(1:4));

YZ = [subY,Z];

R = corrcoef([T,YZ]);
r = R(1,2:15);
r = transpose(r);
r2 = diag(r*transpose(r));

N = length(T);
t = r*sqrt(N-2)./sqrt(1-r2);
v = N-1;
p = 2*tcdf(-abs(t),v);


disp("相関係数:")
disp(r)
figure
bar(r)

strImp = {'冷たい', '利他的な', '頑固な', '嫌い', '支配的な', '下品な', '強い', '理性的な', '陰気な', '消極的な','第1主成分','第2主成分','第3主成分','第4主成分'};
xticklabels(strImp)
ylabel("相関係数")
print('-dpng','election_cor.png');

for i = 1:length(p)
    if p(i)<0.01
        disp(strImp(i)+":優位性がある（p<0.01）")
    else
        if p(i)<0.05
            disp(strImp(i)+":優位性がある(p<0.05)")
        else 
            disp(strImp(i)+":優位性があるとは言えない")
        end
    end
end
%}
%課題6
%{
X = [
    1 0 1 0 1 1 1 1 1
    0 0 0 1 1 0 0 1 0
    1 0 0 0 0 0 1 1 1
    1 1 1 1 1 0 1 1 0
    0 1 0 1 1 1 1 1 0
    1 1 0 1 0 1 1 1 0
    0 0 0 0 0 1 0 0 1
    0 0 0 0 0 1 1 1 1
    1 1 1 0 0 0 1 1 1
    1 1 1 0 1 1 0 1 0
    0 1 1 1 0 1 1 0 0
    1 1 1 0 1 1 1 0 1
    0 0 0 0 1 1 0 0 1
    0 1 1 0 1 0 1 0 0
    0 1 1 0 1 0 1 1 1
    ];
%{
%1の数の分だけの長さの行列を作る
x = zeros(ones(1,size(X,1))*X*ones(size(X,2),1),2);

counter = 1;
for i = 1:size(X,1)
    for j = 1:size(X,2)
        if X(i,j)
            x(counter,:) = [i,j];
            counter = counter+1;
        end
    end
end

a = x(:,1);
b = x(:,2);
%}


da = X*ones(size(X,2),1);
db = transpose(X)*ones(size(X,1),1);
Da = diag(da);
Db = diag(db);
Da_sub1 = diag(power(diag(Da),0.5));
Db_sub1 = diag(power(diag(Db),0.5));
Da_sub2 = diag(power(diag(Da),-0.5));
Db_sub2 = diag(power(diag(Db),-0.5));



du = Da_sub2*da./norm(Da_sub2*da,2);
dv = Db_sub2*db./norm(Db_sub2*db,2);
Z = (eye(size(du,1))-du*transpose(du))*Da_sub2*X*Db_sub2*(eye(size(dv,1))-dv*transpose(dv));



[U,S,V] = svd(Z);


result_a = Da_sub2*U;
result_b = Db_sub2*V;

sample_str = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"];
category_str = ["明るい","温かい","かたい","重い","人工的","上品","単純","強い","汚い"];


%サンプルプロット
x = result_a(:,1);
y = result_a(:,2);

figure
scatter(x,y,'rx')
xlabel("第1主成分")
ylabel("第2主成分")
title("サンプルプロット")
text(x,y,sample_str)
print('-dpng','exp3_2dplots_1.png');
%カテゴリプロット
x = result_b(:,1);
y = result_b(:,2);

figure
scatter(x,y,'rx')
xlabel("第1主成分")
ylabel("第2主成分")
title("カテゴリプロット")
text(x,y,category_str)
print('-dpng','exp3_2dplots_2.png');

target_a = result_a(:,1);
target_b = result_b(:,1);



figure
hold on
%破線のグリッドを表示
for i = 1 : size(target_a,1)
    yline(target_a(i),'--')
end

for j = 1: size(target_b,1)
    xline(target_b(j),'--')
end

%各点ごとのラベルを表示
%{
xticks(sort(target_b))

yticks(sort(target_a))
%}

for i = 1 : size(target_a,1)
    for j = 1: size(target_b,1)
        if X(i,j)
            scatter(target_b(j),target_a(i),'ko')
        end
    end
end
title("並び変えた後のデータ行列")



%{
[sorted_a,Ia] = sort(result_a1);
[sorted_b,Ib] = sort(result_b1);

sorted_Xa = X;
sorted_Xab = X;
for i = 1:size(X,2)
    sorted_Xa(:,i) = X(Ia,i);
end

for i = 1:size(X,1)
    sorted_Xab(i,:) = sorted_Xa(i,Ib);
end
%}

%}