fs= 16000;
f = 1000;


fid = fopen("左上目のあ.raw","r");
x = fread(fid,'int16');
fclose(fid);
%8000～18000 あ
%20000～30000 い
%33000～44000 う
%46000～57000 え
%60000～75000 お

a = x(13001:14024);
%i = x(25001:26024);
%u = x(38001:39024);
%e = x(53001:54024);
%o = x(68001:69024);


focus = a;

h = zeros(1,1024);

A = lpc(a,20);

imp = zeros(1,1044);
imp(21) = 10000000;


for n = 1:1024
    h(n) = A(1)*imp(n);
    for m = 1:20
        if n-m >0
            h(n) = h(n)-A(m+1)*h(n-m);
        end
    end
end

w = hamming(1024);
l = 512;
L = 1024;

%plot(h)
hold on
periodogram(a,w,L,fs)
periodogram(h,w,L,fs)
hold off
%specgram(h,l,fs)


%xlabel('時間[t](16000=1秒)')
%ylabel('声の大きさの振幅[bit]')

%saveas(gcf,'5-3-1','epsc')

%xlabel('周波数[kHz]')
%ylabel('パワー/周波数[dB/Hz]')

%saveas(gcf,'5-3-1','epsc')

%xlabel('録音開始からの時間[t]')
%ylabel('周波数[kHz]')

%saveas(gcf,'5-3-6','epsc')

