fs= 16000;
f = 1000;

fid = fopen("ssss.wav","r");
x = fread(fid,'int16');
fclose(fid);
plot(x)


w = hamming(1024);
l = 512;
L = 1024;

%plot(x(21000:26000))
periodogram(x(30001:31024),w,l,fs)
%specgram(x,l,fs)

%xlabel('時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'4-2-2','epsc')

xlabel('周波数[kHz]')
ylabel('パワー/周波数[dB/Hz]')

saveas(gcf,'4-2-3','epsc')


