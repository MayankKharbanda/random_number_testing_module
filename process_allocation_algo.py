import config
from sys import exit
    

def process_alloc(Tests, CORES):
    
    '''

    Parameters
    ----------
    Tests : the list of tests to be run.
    
    CORES : number of cores on which tests are to be run
            

    Returns
    -------
    process_list : A list containing 'n' lists, for 'n' cores, 
                    of tests for running on each core.
                
    -1 :  If running time for even a single test is not
            available.

    '''
    
    
    
    #check if run time exists in the Tests list, else return -1.
    for test in range(len(Tests)):
        if(Tests[test][config.TIME]=='None'):
            return -1
                

    
    
    
    process_list = []       #list of lists containing tests to run on processes

    
    #Copy test list so that original list doesn't get affected
    tests_copy = Tests.copy()



    #create process list for each core.
    for _ in range(CORES):
        process_list.append([])


    

    
    try:
        #sorting list wrt time to execute
        tests_copy.sort(key = lambda x:float(x[config.TIME]))
    except:
        print(f'!!! Error test time could not be evaluated. !!!')
        exit()
    
    
    
    
    
    total_time = 0     #summation of wait time of all the processors


    
    
    
    #Total time required to execute (x-n) tests, where x is total number 
    #of tests, and n is the number of cores in the list.
    if(len(tests_copy)>CORES):
        total_time = sum(float(test[config.TIME]) for test in tests_copy[:-CORES])


    
    
    
    #wait time for each processor/time taken to start last test on the process
    approx_time_each_process = total_time/CORES


    
    
    
    #adding slowest tests to each core list
    for i in range(CORES):
        if(len(tests_copy)>0):
            process_list[-(i+1)].insert(0, tests_copy[-1])
            del tests_copy[-1]






    #adding tests to all the core tests lists except the first one
    #in greedy algorithm.
    for i in range(CORES-1):
        
        if(len(tests_copy) == 0):
            break
        
        temp_sum = float(tests_copy[-1][config.TIME])   #first try to add long tests in the list
        process_list[-(i+1)].insert(0, tests_copy[-1])
        del tests_copy[-1]
        
        if(len(tests_copy) == 0):
            break
        
        while((temp_sum + float(tests_copy[-1][config.TIME])) <= approx_time_each_process):     #first try to add long tests in the list
            temp_sum = temp_sum + float(tests_copy[-1][config.TIME])
            process_list[-(i+1)].insert(0, tests_copy[-1])
            del tests_copy[-1]
            if(len(tests_copy) == 0):
                break
        
        if(len(tests_copy) == 0):
            break
        
        temp_sum = temp_sum+float(tests_copy[0][config.TIME])
        j = 0
        
        while(temp_sum < approx_time_each_process):     #add fast tests in the list
            process_list[-(i+1)].insert(j, tests_copy[0])
            del tests_copy[0]
            j = j+1
            if(len(tests_copy) == 0):
                break
            temp_sum = temp_sum+float(tests_copy[0][config.TIME])



    #adding all left over tests to the first core
    j=0
    while(len(tests_copy)!=0):
        process_list[0].insert(j,tests_copy[0])
        j = j+1
        del tests_copy[0]
    
    
    
    return process_list