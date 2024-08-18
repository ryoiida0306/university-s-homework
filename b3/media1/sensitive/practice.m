clear all;
close all;

load('practice.mat');
addpath('plotting_function');
addpath('statistical_function');


%練習問題１


disp("mean(Y)=")
disp(mean(Y))

disp("var(Y)=")
disp(var(Y))

disp("sqrt(var(Y))=")
disp(sqrt(var(Y)))

sort(Y);

disp("min(Y)=")
disp(min(Y))

disp("4分の1分位=")
disp((Y(125,[1,2,3,4])+Y(126,[1,2,3,4]))/2)

disp("中央値=")
disp((Y(250,[1,2,3,4])+Y(251,[1,2,3,4]))/2)

disp("4分の3分位=")
disp((Y(125+250,[1,2,3,4])+Y(126+250,[1,2,3,4]))/2)

disp("max(Y)=")
disp(max(Y))

%練習問題2~5

%練習問題2
for i = 1:4 
    subplot(3,4,i)
    plot(Y(:,i),0,'rx')
    xlim([-4,4])
    title("Variable"+i)
%練習問題3
    subplot(3,4,i+4)
    myboxplot_x(Y(:,i));
    xlim([-4,4])
    grid on;
    title("Variable"+i)
%練習問題4
    subplot(3,4,i+8)
    histogram(Y(:,i),9);
    xlim([-4,4])
    ylim([0,150])
    ylabel("frequency")
    grid on
    title("Variable"+i)
end


%練習問題6

for i = 1:3
    disp(i+"vs4")
    E=mean(Y(:,i)-Y(:,4));
    V=var(Y(:,i)-Y(:,4),0);
    s=sqrt(V);
    N=length(Y(:,1));
    t=E*sqrt(N)/s;
    v=N-1;
    p = 2*tcdf(-abs(t),v);
    disp("差の平均値　="+E)
    disp("差の不偏分散="+V)
    disp("差の標準偏差="+s)
    disp("t="+t)
    disp("自由度="+v)
    disp("p値="+p)
    if p<0.01
        disp("優位性がない（p<0.01）")
    else
        if p<0.05
            disp("優位性がない(p<0.05)")
        else 
            disp("優位性がないとは言えない")
        end
    end
    
end


%練習問題8
for i = 1:3
    figure
    scatter(Y(:,i),Y(:,4),3,'filled')
end



%練習問題9

for i = 1:3
    x = Y(:,i);
    y = Y(:,4);
    Cov = cov([x,y],1);
    Covxy =Cov(1,2);
    r = corrcoef([x,y]);
    R = r(1,2);
    N = length(Y(:,1));
    t = R*sqrt(N-2)/sqrt(1-R*R);
    v=N-1;
    p = 2*tcdf(-abs(t),v);
    %H0:r=0

    disp("共分散="+Covxy)
    disp("相関係数="+R)
    disp("t値="+t)
    disp("自由度="+(N-2))
    disp("p値="+p)
     if p<0.01
        disp("優位性がない（p<0.01）")
    else
        if p<0.05
            disp("優位性がない(p<0.05)")
        else 
            disp("優位性がないとは言えない")
        end
    end

end

%練習問題10

disp(cov([Y(:,1),Y(:,2),Y(:,3),Y(:,4)]))


%練習問題11

Sig = cov([Y(:,1),Y(:,2),Y(:,3),Y(:,4)]);
[V,D] = svd(Sig);
lamda = zeros(1,4);
lamSum = 0;
for i = 1:4
    lamda(i) = D(i,i);
    lamSum =lamSum+D(i,i);
end

Con = lamda/lamSum;
AcCon = zeros(1,4);
for i = 1:4
    for j = 1:i
        AcCon(i) = AcCon(i)+Con(j);
    end
end

%disp("固有ベクトル="+V)
%disp("固有値="+lamda)
%disp("寄与率="+Con)
%disp("累積寄与率="+AcCon)

disp(V)
disp(lamda)
disp(Con)
disp(AcCon)

%練習問題12

Sig = cov([Y(:,1),Y(:,2),Y(:,3),Y(:,4)]);
[V,D] = svd(Sig);

I = eye(500);
One = ones(500);
Y_childa = (I-One/500)*Y;
Z = Y_childa*V;

figure
scatter(Z(:,1),Z(:,2),5,'filled')

for i = 1:4
    disp(mean(Z(:,i)))
end
disp(var(Z,1))
disp(cov(Z))


