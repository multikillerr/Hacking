import sys
import os
import shutil
filename=raw_input("Enter the name of the file: ")
def file1(file):
    file=open(filename,"r")
    for line in file:
        lines=line[17:30]
        with open("keys.txt","a") as f:
            f.write(lines)
            f.write("\n")
            os.system("./unexpect "+lines)
file1(file)
