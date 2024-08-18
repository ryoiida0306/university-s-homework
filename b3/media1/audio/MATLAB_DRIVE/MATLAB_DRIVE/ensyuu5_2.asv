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


focus = a;

h = zeros(1,1024);

A = lpc(a,20);

imp = zeros(1,1044);
imp(21) = 1;

for n = 1:1024
    h(n) = A(1)*imp(n);
    for m = 1:20
        if n-m >0
            h(n) = h(n)-A(m+1)*h(n-m);
        end
    end
end

plot(h)


xlabel('h[i]の変数i')
ylabel('LPC分析から導いたインパルス応答h[i]')

saveas(gcf,'5-2-1','epsc')


