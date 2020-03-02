import numpy as np
#import sys

with open('dieharder_203.bin','wb') as f:
    for _ in range(1_000_000_00):
        f.write(np.random.bytes(4))