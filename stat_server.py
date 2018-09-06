# !/usr/bin/python
import os
import struct

FORMAT = "<IIIIIIIIII"

stat = os.stat('algorithm.py')

print(stat)

#packed = struct.pack(FORMAT, stat)
#unpacked = struct.unpack(FORMAT, packed)

#print(unpacked)

for i in dir(stat):
    if i.startswith("st_"):
        if not i.endswith("_ns"):
            print(i)
