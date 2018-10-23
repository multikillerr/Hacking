#!usr/bin/python27
import sys
import socket
import os
s=socket.socket(sock.AF_INET, sock_STREAM)
try:
    connection=s.bind(127.0.0.1, 8000)
except:
    print("Could not bind on the ip provided")
while True:
    data=s.recv(1024)
    print data
