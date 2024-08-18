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


disp(lpc(a,20));





%xlabel('録音開始からの時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'4-1-3','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'4-1-4','epsc')

xlabel('a[i]の変数i')
ylabel('LPC分析の係数a[i]')

saveas(gcf,'5-1-1','epsc')





