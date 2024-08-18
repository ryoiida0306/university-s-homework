fs = 16000;

fid = fopen("有声音.raw","r");
x = fread(fid,"int16");

fid = fopen("無声音.raw","r");
y = fread(fid,"int16");

soundsc(x,fs)

w=hamming(10000);
l = 512;
L = 1024;
x = x(35000:44999);
y = y(30000:39999);


periodogram(x,w,L,fs)
title("有声音のスペクトル")

%specgram(y,l,fs);
%title("無声音のスペクトログラム")