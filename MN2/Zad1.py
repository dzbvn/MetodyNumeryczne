import numpy as np
import matplotlib.pyplot as plt

print(10.0**16)
print(10.0**16+1)

print(10.0**15)
print(10.0**15+1)

#print(np.finfo(float))

print(1.25.hex())

import struct
def double_to_hex(f):
    print(hex(struct.unpack('<Q', struct.pack('<d', f))[0]))
double_to_hex(1.0)

print(int('3ff', 16))