fid = fopen('boin.raw','r');
x = fread(fid,'int16');

dataLength = length(x);

%echo
y = zeros(dataLength:1);
y(1)=1;
y(800)=0.7;
y(1600)=0.3;

z=conv(x,y);

plot(z(9000:20000))

xlabel('時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')

saveas(gcf,'2-2-2','epsc')


