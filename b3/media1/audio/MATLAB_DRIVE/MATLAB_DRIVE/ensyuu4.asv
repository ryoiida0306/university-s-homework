fs= 16000;
f = 1000;

fid = fopen("boin.raw","r");
x = fread(fid,'int16');
fclose(fid);
%8000～18000 あ
%20000～30000 い
%33000～44000 う
%46000～57000 え
%60000～75000 お

a = x(13001:14024);
i = x(25001:26024);
u = x(38001:39024);
e = x(53001:54024);
o = x(68001:69024);

w = hamming(1024);
l = 512;
L = 1024;

%plot(a)
%periodogram(i,w,L,fs);
specgram(x,l,fs);

%xlabel('録音開始からの時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'4-1-3','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'4-1-4','epsc')

xlabel('録音開始からの時間[t]')
ylabel('周波数[kHz]')

saveas(gcf,'4-1-5','epsc')


