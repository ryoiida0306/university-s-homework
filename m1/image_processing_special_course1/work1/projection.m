% Make 3D object
close all;
N1 = 40; XX1 = []; 
for i=1:N1, XX1 = [XX1; [-5, -5+10*i/N1, -5]]; end
for i=1:N1, XX1 = [XX1; [ 5, -5+10*i/N1, -5]]; end
for i=1:N1, XX1 = [XX1; [-5, -5+10*i/N1,  5]]; end
for i=1:N1, XX1 = [XX1; [ 5, -5+10*i/N1,  5]]; end
for i=1:N1, XX1 = [XX1; [-5+10*i/N1/2, 5+10*i/N1/2, -5]]; end
for i=1:N1, XX1 = [XX1; [ 5-10*i/N1/2, 5+10*i/N1/2, -5]]; end
for i=1:N1, XX1 = [XX1; [-5+10*i/N1/2, 5+10*i/N1/2,  5]]; end
for i=1:N1, XX1 = [XX1; [ 5-10*i/N1/2, 5+10*i/N1/2,  5]]; end
for i=1:N1, XX1 = [XX1; [-5+10*i/N1, -5, -5]]; end
for i=1:N1, XX1 = [XX1; [-5+10*i/N1, -5,  5]]; end
for i=1:N1, XX1 = [XX1; [-5, -5, -5+10*i/N1]]; end
for i=1:N1, XX1 = [XX1; [ 5, -5, -5+10*i/N1]]; end
for i=1:N1, XX1 = [XX1; [-5,  5, -5+10*i/N1]]; end
for i=1:N1, XX1 = [XX1; [ 5,  5, -5+10*i/N1]]; end
for i=1:N1, XX1 = [XX1; [ 0, 10, -5+10*i/N1]]; end
XX1=XX1';
[m,n]=size(XX1);
XX1h = [XX1;ones(1,n)];

thx = -15*pi/180; thy = 30*pi/180; thz = -5*pi/180;
RX = [1,0,0;0,cos(thx),-sin(thx);0,sin(thx),cos(thx)];
RY=[cos(thy),0,sin(thy);0,1,0;-sin(thy),0,cos(thy)];
RZ=[cos(thz),-sin(thz),0;sin(thz),cos(thz),0;0,0,1];
R=RX*RY*RZ; 
Tz = 500; T = [0;0;Tz]; 
M=[[R,T];0,0,0,1];
XXh = M*XX1h;
XX = [XXh(1,:);XXh(2,:);XXh(3,:)];

% Plot 3D object
figure;
plot3(XX(1,:), XX(2,:), XX(3,:),'.');
view(20, 70);

% Camera matrix
Pp = [1 0 0 0; 0 1 0 0; 0 0 1 0];
Pa = [1/Tz 0 0 0; 0 1/Tz 0 0; 0 0 0 1];

% projection
xx1h = Pp*XXh./XX(3,:);
% affine
xx2h = Pa*XXh;

xx1 = [xx1h(1,:);xx1h(2,:)];
xx2 = [xx2h(1,:);xx2h(2,:)];

% Plot 2D
figure;
plot(xx1(1,:), xx1(2,:),'b.');
hold on;
plot(xx2(1,:), xx2(2,:),'r.');
hold off;

%結果
%Tzを大きくするにつれて，透視投影と弱透視投影による写像が重なるように近づいた．

%考察
%射影カメラでは，非線形ではあるが立体のZ座標の情報をそのままもちいて透視投影していた．
%比べてアフィンカメラでは，線形ではあるが立体のZ座標をそのまま用いず，
%一度カメラ座標におけるz = Tzのスクリーンに正射影してから透視投影していた．
%つまり，立体のZ座標という奥行きの情報をなくすかなくさないかの違いである．
%この違いが物体を見た時にどのように影響するかを考えると，物体を近くで見た時には
%Z座標の有無，つまり奥行きによる立体感の違いが生まれるが，
%物体を遠くから見た時にはあまり違いが見られないことが考えられる．
%よって，Tzを変化させたときに結果のようになる理由は，
%物体を近くから見ると奥行きの情報が大きく影響し，
%物体を遠くから見た時は奥行きの影響が少ないことを表していると考察した．

