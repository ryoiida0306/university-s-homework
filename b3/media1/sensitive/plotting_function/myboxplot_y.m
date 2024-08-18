function myboxplot(Y)

if iscell(Y)
  X = Y;
else
  if size(Y,1) >= size(Y,2)
    X = num2cell(Y,1);
  else
    X = num2cell(Y',1);
  end
end

ID = 1:length(X);

ms = 5;
lw = 1;
color1 = 'r';
color2 = 'b';
color3 = 'k';

w = 0.4;
s = 0.2;

R = length(X);

%figure()
hold on

for id=1:R

  r = ID(id);

  x = X{id};
  N = length(x);
  id1 = floor(N/4)+1;
  id2 = floor(N/2)+1;
  id3 = floor(N*3/4)+1;
 
  y = sort(x);

  x_min = y(1);
  x_1qt = y(id1);
  x_2qt = y(id2);
  x_3qt = y(id3);
  x_max = y(N);

  X_max_row(id) = x_max;
  X_min_row(id) = x_min;

  IQR = x_3qt - x_1qt;
  upp = x_3qt + 1.5*IQR;
  low = x_1qt - 1.5*IQR;

  x_upp = max(y(y < upp));
  x_low = min(y(y > low));

  outliers = [y(y>upp)' y(y<low)'];

  line([r-w r+w],[x_2qt x_2qt],'linewidth',2*lw,'color',color1)
  line([r-w r+w],[x_1qt x_1qt],'linewidth',1*lw,'color',color2)
  line([r-w r+w],[x_3qt x_3qt],'linewidth',1*lw,'color',color2)
  line([r-w r+w],[x_3qt x_3qt],'linewidth',1*lw,'color',color2)
  line([r-s r+s],[x_upp x_upp],'linewidth',1*lw,'color',color2)
  line([r-s r+s],[x_low x_low],'linewidth',1*lw,'color',color2)
  line([r r],[x_3qt x_upp],'linewidth',1*lw,'color',color2)
  line([r r],[x_1qt x_low],'linewidth',1*lw,'color',color2)
  line([r-w r-w],[x_1qt x_3qt],'linewidth',1*lw,'color',color2)
  line([r+w r+w],[x_1qt x_3qt],'linewidth',1*lw,'color',color2)

  if ~isempty(outliers)
    plot(r*ones(1,length(outliers)),outliers,'o','color',color3,'linewidth',lw,'markersize',ms)
  end

end

X_max = max(X_max_row);
X_min = min(X_min_row);
inter= ( X_max - X_min )*0.2;

axis([0, max(ID)+1, X_min-inter, X_max+inter])

hold off



