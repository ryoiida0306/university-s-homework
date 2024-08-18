

freqz([1,0,1]);

y = conv([1,0,1], [1,-1]);
disp(y)

fs = 16000;
data = audioread('msksda06.wav');
filtered_data = conv(data,[1,-1]);
soundsc(data,fs)

zplane([1,0,1],[1,0]);