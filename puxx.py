import os
import random

def flip_byte(in_bytes):
    i=random.randint(0,len(in_bytes))
    c=chr(random.randint(0,0xff))
    return in_bytes[:i]+c+in_bytes[i+1:]

print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
print flip_byte("AAAAAAAAAA")
