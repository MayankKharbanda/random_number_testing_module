#import math

'''
def rounder(number):
    digits_in_number = len(number)
    round_offset = 2 * pow(10, digits_in_number-2)
    number = int(number)+round_offset
    number = number/pow(10, digits_in_number-2)
    number = math.floor(number)
    number = number * pow(10, digits_in_number-2)
    return number
'''

'''
with open('results/results numpy-random/TestU01/bytes_small_crush.txt', 'r') as fn, open('config2.txt', 'r') as fr, open('config3.txt','w+') as fw:
    
    for line_bytes in fn.readlines():
        number = rounder(line_bytes.strip())
        line_config = fr.readline()
        
        line_config = line_config.strip()
        line_config = line_config +'\t\t'+ str(number) + "\n"
        fw.write(line_config)
'''
'''
with open('results/results numpy-random/TestU01/bytes_crush.txt', 'r') as fn, open('config2.txt', 'r') as fr, open('config3.txt','a+') as fw:
    line_config = fr.readline()
    while 'smallcrush' in line_config:
        line_config = fr.readline()
    for line_bytes in fn.readlines():
        number = rounder(line_bytes.strip())
        
        line_config = line_config.strip()
        line_config = line_config +'\t\t'+ str(number) + "\n"
        fw.write(line_config)
        line_config = fr.readline()
'''
'''
with open('results/results numpy-random/TestU01/bytes_big_crush.txt', 'r') as fn, open('config2.txt', 'r') as fr, open('config3.txt','a+') as fw:
    line_config = fr.readline()
    while 'smallcrush' in line_config:
        line_config = fr.readline()
    while '\tcrush' in line_config:
        line_config = fr.readline()
    for line_bytes in fn.readlines():
        number = rounder(line_bytes.strip())
        
        line_config = line_config.strip()
        line_config = line_config +'\t\t'+ str(number) + "\n"
        fw.write(line_config)
        line_config = fr.readline()
'''
with open('config2.txt', 'r') as fr, open('config3.txt','a+') as fw:
    line_config = fr.readline()
    while 'nist' not in line_config:
        line_config = fr.readline()
    
    while 'nist' in line_config:
        line_config = line_config.strip()
        line_config = line_config +'\t\t25,000,000\n'
        fw.write(line_config)
        line_config = fr.readline()