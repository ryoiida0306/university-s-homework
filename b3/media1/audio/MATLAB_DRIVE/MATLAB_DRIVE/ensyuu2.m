fid = fopen('boin.raw','r');
x = fread(fid,'int16');
plot(x)

L = length(x);

%fade in
fIn = zeros(L,1);
for t = 1:L
    fIn(t) = t/L*x(t);
end


%fade out
fOut = zeros(L,1);
for t = 1:L
    fOut(t) = (L-t)/L*x(t);
end

%plot(fIn)
plot(fOut)

xlabel('録音開始からの時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')

saveas(gcf,'2-1-2','epsc')