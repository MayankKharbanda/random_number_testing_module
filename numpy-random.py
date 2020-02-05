import numpy as np
import sys

with open(sys.argv[1],'wb') as f:
    for _ in range(1_000_000_00):
        f.write(np.random.bytes(4))