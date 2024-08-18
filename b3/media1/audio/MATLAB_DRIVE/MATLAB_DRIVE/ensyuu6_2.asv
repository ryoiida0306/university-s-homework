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

T = 16000*3;

palse = zeros(1,T);
for t = 1:T
    if rem(t,1000)==0%パルス波のHzの調節
        palse(t) = 1;
    end
end


w = hamming(1024);
l = 512;
L = 1024;
LPC = lpc(a,20);

y = zeros(1,T);
for n = 1:T
    y(n) = LPC(1)*palse(n);
    for m = 1:20
        if n-m >0
            y(n) = y(n)- LPC(m+1)*y(n-m);
        end
    end
end

plot(y(1:1000))
periodogram(y(1:1024),w,L,fs)
%soundsc(y,16000)




xlabel('時間[t](16000=1秒)')
ylabel('声の大きさの振幅')

saveas(gcf,'6-2-2','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'6-2-3','epsc')

%xlabel('録音開始からの時間[t]')
%ylabel('周波数[kHz]')

%saveas(gcf,'6-3-6','epsc')


