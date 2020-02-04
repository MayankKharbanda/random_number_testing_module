import random
import struct
#import numpy as np
import sys
while (True):
    sys.stdout.buffer.write(struct.pack('>I', random.randint(0, 2**32)))
    #sys.stdout.buffer.write(struct.pack('>I', random.randint(0, 2**32)))
#import numpy as np
#import sys
#import time

#if(len(sys.argv)!=2):
   # print('!!!Error no output file alloted.')
#else:
#with open(sys.argv[1],'wb') as f:
#while(True):
    #sys.stdout.write(np.random.bytes(1))
           #time.sleep(1)
#print(random.randint(0, 2**32))