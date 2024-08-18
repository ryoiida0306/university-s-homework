fs= 16000;
f = 1000;

fid = fopen("hi.wav","r");
x = fread(fid,'int16');
fclose(fid);
plot(x)
w = hamming(1024);
l = 512;
L = 1024;

plot(x(15000:17500))
%periodogram(x(20001:21024),w,L,fs)
%specgram(x,l,fs)


xlabel('時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')

saveas(gcf,'4-3-1','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'4-3-4','epsc')

%xlabel('録音開始からの時間[t]')
%ylabel('周波数[kHz]')

%saveas(gcf,'4-3-6','epsc')



