fid = fopen('siin.raw','r');
x = fread(fid,'int16');



plot(x)
xlabel('録音開始からの時間[t](16000=1秒)')
ylabel('声の大きさの振幅[bit]')


saveas(gcf,'1','epsc')
%録音可能な最高周波数、はサンプリング周波数は16000だから、8000未満
