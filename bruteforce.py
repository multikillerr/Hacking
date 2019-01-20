import os
os.system("touch payload.txt")
filename='payload.txt'
f=open(filename,'w')
for line in range(0,10001):
    f.write(str(line))
    f.write("\n")
f.close()

