import shutil
import os
filename=raw_input("Enter file name: ")
f=open(filename,'r')
for line in f:
    line=int(line,16)
    #line=str(line)
    print line 
