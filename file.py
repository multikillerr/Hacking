filename=raw_input("Enter the file name: ")

def file1(file):
    file=open(filename,"r")
    for line in file:
        lines=line[0:8]
        with open("Test1.txt","a") as f:
            f.write(lines)
            f.write("\n")
def file2(file):
    
    file=open(filename,"r")
    for line in file:
        lines=line[9:49]
        with open("Test2.txt","a") as g:
            g.write(lines)
            g.write("\n")
def file3(file):  
    file=open(filename,"r")   
    for line in file:
        lines=line[51:66]
        with open("Test3.txt","a") as h:
            h.write(lines)
            h.write("\n")
file1(file)
file2(file)
file3(file)
