
fid = fopen("yokkora.raw","r");
x = fread(fid,'int16');
fclose(fid);


plot(x(120001:121024))
l = 512;
specgram(x,l,fs);

xlabel('録音開始からの時間[t]')
ylabel('周波数[kHz]')

saveas(gcf,'3-3-1','epsc')

%xlabel('録音開始からの時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'3-2-1','epsc')
