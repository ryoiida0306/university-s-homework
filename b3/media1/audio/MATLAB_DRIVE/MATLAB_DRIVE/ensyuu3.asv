fs= 16000;
f = 1000;

x = zeros(1024,1);

for t = 1:1024
    x(t) = sin(t/fs*f*2*pi);
end

l = 1024;
w = hamming(1024);

plot(x(1:100))
%periodogram(x,w,l,fs)

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'3-1-2','epsc')

xlabel('録音開始からの時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')

saveas(gcf,'3-1-1','epsc')




