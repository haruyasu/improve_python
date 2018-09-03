# !/usr/bin/python
import os
import struct

FORMAT = "<IIIIIIIIII"

stat_data = os.stat('algorithm.py')
packed = struct.pack(FORMAT, stat_data)
unpacked = struct.unpack(FORMAT, packed)


print(unpacked)
