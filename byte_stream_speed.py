import random
import struct
import sys
for _ in range(1024*256):
    sys.stdout.buffer.write(struct.pack('>I', random.randint(0, 2**32)))
