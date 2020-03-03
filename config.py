
'''
Variable contains the details of indices in the list of tests.
'''

SUITE = 0
NAME = 1
ID = 2
TIME = 3
SIZE = 4
N_TUPL = 5




TESTS_FILE = 'config.txt'   #contains location of the configuration file.

#contains location of random source.
RANDOM_SOURCE = 'random_numbers_time/dieharder203.bin'   


#contains location where results are to be stored
RESULT_DEST = 'results_parallel_process'


#number of cores to run the tests
CORES = 4


#destination for random file generation
TEMP_DEST = 'temp_dest'


#maximum file size in bytes that can be generated
MAX_FILE_SIZE = 5_400_000_000