import sys
import os

# 上層ディレクトリのパスを取得
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.pathに追加
sys.path.append(parent_dir)

import numpy as np
from filename import fname, fpath

with open('{}.wav'.format(fpath), 'rb') as f:
    data = f.read()

mystr = ""
fdata = np.zeros(len(data))
i = 0
t = 0
while i < len(data)-1 :
    datai = int(data[i])
    if i <= 44 :
        if  (65 <= datai <= 90 or 97 <= datai <= 122) :
            mystr = mystr + " " + chr(datai)
        else :
            mystr = mystr + " " + str(datai)
        i += 1
    else :
        datai *=256
        datai += int(data[i+1])
        if datai > 32767 :
            datai -= 65536
        mystr = mystr + " " + str(datai)
        fdata[t] = datai
        t += 1
        i += 2

if __name__ == "__main__" :
    with open('{}.txt'.format(fname), 'w') as output_file:
        
        output_file.write(mystr)
