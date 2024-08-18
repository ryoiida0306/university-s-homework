fid = fopen('boin.raw','r');
x = fread(fid,'int16');
plot(x)

L = length(x);

N = 10;

z = zeros(L,1);


for t=N+1:L
    for n = 1:N
        z(t) = z(t)+x(t-n);
    end
    z(t) = z(t)/N;
end

plot(z(9000:20000))

xlabel('時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')

saveas(gcf,'2-3-2','epsc')

soundsc(z,fs)


