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

aa = x(8001:18000);
a = x(13001:14024);
i = x(25001:26024);
u = x(38001:39024);
e = x(53001:54024);
o = x(68001:69024);

T = 16000*3;

Rand = randn(T,1);

w = hamming(1024);
l = 512;
L = 1024;
LPC = lpc(i,20);

y = zeros(1,T);
for n = 1:T
    y(n) = LPC(1)*Rand(n);
    for m = 1:20
        if n-m >0
            y(n) = y(n)- LPC(m+1)*y(n-m);
        end
    end
end

plot(Rand)
%periodogram(y(1:1024),w,L,fs)
%soundsc(y,16000)



xlabel('時間[t](16000=1秒)')
ylabel('声の大きさの振幅')

saveas(gcf,'6-1-1','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'6-1-3','epsc')

%xlabel('録音開始からの時間[t]')
%ylabel('周波数[kHz]')

%saveas(gcf,'6-1-6','epsc')




