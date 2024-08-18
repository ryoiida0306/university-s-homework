clc; clear; close all;

%-------------------------------------------------------

x = 0;
y = 0;
z = 0;

figure('Position',[800 700 600 900]);
movegui(gcf,'center');

subplot(2,1,1);
h1 = bar([x y z],'FaceColor',[0 0.4 0.85],'EdgeColor','none');
ylim([-1.2 1.2]);
set(gca,'YGrid','on');
set(gca,'xticklabel',{'x','y','z'});
xlabel('axis','FontSize',12);
ylabel('acceleration (g)','FontSize',12);
title('STM32F4-LIS3DSH Accelerometer');

subplot(2,1,2);
h2 = plot(x,'Color',[1 0 0]); hold on;
h3 = plot(y,'Color',[0 0.5 0]);
h4 = plot(z,'Color',[0 0 1]); hold off;
h5 = gca;
xlabel('time (samples)','FontSize',12);
ylim([-1.5 1.5]);
set(gca,'YGrid','on');
ylabel('acceleration (g)','FontSize',12);
title('STM32F0-LIS3DSH (RGB = XYZ)');

N = 100;	% horizontal scale span
t = 1;
k = [1 N];
xlim(k);

%-------------------------------------------------------

fclose(instrfind);
s = serial('COM6','BaudRate',921600,'FlowControl','hardware');
fopen(s);
s.ReadAsyncMode = 'continuous';

fwrite(s,1);	% disable previous transmission
fwrite(s,0);	% start current transmission

while t<1e6;
	if(s.BytesAvailable >= 6)
		n1 = fread(s,2);
		n2 = fread(s,2);
		n3 = fread(s,2);
		
		i1 = typecast(uint8(n1),'int16');
		i2 = typecast(uint8(n2),'int16');
		i3 = typecast(uint8(n3),'int16');
		
		x = single(i1)/16384;
		y = single(i2)/16384;
		z = single(i3)/16384;

		set(h1,'YData',[x y z]);
		
		set(h2,'YData',[get(h2,'YData') x]);
		set(h3,'YData',[get(h3,'YData') y]);
		set(h4,'YData',[get(h4,'YData') z]);
				
		t = t+1;
		if(t>N)
			k = k+1;
			set(h5,'XLim',k);
		end
		
		drawnow;
	end
end

fwrite(s,1);

