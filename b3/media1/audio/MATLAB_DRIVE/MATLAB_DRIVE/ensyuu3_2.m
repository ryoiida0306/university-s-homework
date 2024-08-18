fs= 16000;
fx = 2000;
fy = 3000;

x = zeros(1024,1);
y = zeros(1024,1);

for t = 1:1024
    x(t) = sin(t/fs*fx*2*pi);
    y(t) = sin(t/fs*fy*2*pi);
end
z = x+y;

l = 1024;
w = hamming(1024);

plot(z(1:100))
periodogram(z,w,l,fs)

%periodogram(x,w,l,fs)

xlabel('周波数[kHz]')
ylabel('パワー/周波数[dB/Hz]')

saveas(gcf,'3-2-2','epsc')

%xlabel('録音開始からの時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'3-2-1','epsc')

