
'''
Variable contains the details of indices in the list of tests.
'''

SNO = 0
SUITE = 1
NAME = 2
ID = 3
TIME = 4
SIZE = 5
N_TUPL = 6




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


'''
config function is used to initialize the tests list from config file, 
passed as parameter.
'''


def config(file):
    
    '''
    input: path of configuration file from which data is to be taken.
    output: returns a list of all the tests to be run on the random numbers.
    NOTE: The code is # sensitive, if there is # at any position in a line,
        the test will not be considered.
    '''
    
    tests=[]        #contains list of all the tests to be checked.
    
    with open(file,'r') as f:
        for line in f.readlines():
            if('#' in line):        #'#' sensitive.
               continue
            tests.append(line.split(','))
           
    for test in range(len(tests)):
        for data in range(len(tests[test])):
            tests[test][data] = tests[test][data].strip()
        tests[test][SIZE] = str(eval(tests[test][SIZE]))      #calculate size of the 
                                                        #file required, if it is 
                                                        #an expression.

    return tests
