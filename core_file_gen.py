import config
import os
import time
from generator import generator_method
from sys import exit
import subprocess






def inorder_random_file_gen(Tests, inorder_file_event, iteration_over_tests, RESULT_DEST, TEMP_DEST, MAX_FILE_SIZE):
    
    
    '''
    

    Parameters
    ----------
    Tests : List of Tests
    inorder_file_event : event for a file generation
    iteration_over_tests : iteration number over the test file
    RESULT_DEST : path where results are stored
    TEMP_DEST : Temporary destination to store the random file
    
    
    Generates random file for a particular test


    Returns
    -------
    None.

    '''
    
    
    
    
    
    temp_random_file = f'{TEMP_DEST}/temp_random.bin'       #creating a temp random file
    start_time = time.time()
    
    
    
    
    
    
    
    
    for test in Tests:
        
        
        #finding the actual name of the random file
        if(test[config.SUITE] == 'dieharder' and 
           (test[config.ID] == '200' 
            or test[config.ID] == '201' 
            or test[config.ID] == '202' 
            or test[config.ID] == '203')):
            
            
            test_file = f'{TEMP_DEST}/{test[config.SUITE]}_{test[config.ID]}_{test[config.N_TUPL]}.bin'
            
        else:
                
            test_file = f'{TEMP_DEST}/{test[config.SUITE]}_{test[config.ID]}.bin'
                
        
        
        
        
        
        file_size = min(int(test[config.SIZE]), MAX_FILE_SIZE)   #calculating size of random file to be generated
        
        
        
        
        try:
            generator_method(temp_random_file, file_size)   #call user defined generator with appropriate parameters
        except:
            print('!!!Cannot generate numbers from generator function!!!')
            exit(0)
        
        
        
        if('False' in subprocess.run(f'test -e {temp_random_file} && echo True || echo False ', stdout=subprocess.PIPE, shell = True).stdout.decode('utf-8')):
            print('!!!Cannot generate numbers from generator function!!!')
            exit(0)
        
        
        
        
        
        os.system(f'mv {temp_random_file} {test_file}')         #changing the name of the file to original name.
        inorder_file_event.set()        #setting the event
        
    
    
    #storing time to generate all the files in an iteration
    os.system(f'mkdir -p {RESULT_DEST}/iteration_{iteration_over_tests}/')
    with open(f'{RESULT_DEST}/iteration_{iteration_over_tests}/file_gen_time.txt','w') as fw:
        fw.write(str(time.time()-start_time))















def random_file_gen_time(process_list, file_gen_queue, total_tests_arr, time_file_event, iteration_over_tests, RESULT_DEST, CORES, TEMP_DEST, MAX_FILE_SIZE):
    
    
    '''
    

    Parameters
    ----------
    process_list : tests list
    file_gen_queue : queue to track currently running tests
    total_tests_arr : total tests in a process list
    time_file_event : event for a file generation
    iteration_over_tests : iteration number
    RESULT_DEST : destination for result
    CORES : core number on which process is running
    TEMP_DEST : temp destination to store the tests

    Generates random file in greedy way, according to earliest requirement
    
    Returns
    -------
    None.

    '''
    
    
    
    start_time = time.time()
    total_tests = sum(total_tests_arr)
    earliest_complete = -1
    temp_random_file = f'{TEMP_DEST}/temp_random.bin'
    current_test_run_arr = [None]*CORES      #current test running in the ith core
    
    
    
    
    last_file_gen_arr = []      #last file generated in a core
    for i in range(CORES):
        last_file_gen_arr.append(-1)
    
    
    
    
    while((sum(last_file_gen_arr)+CORES) < total_tests):      #+1 for array starts from 0
        
        
        while(file_gen_queue.empty() is False):     #getting the current test running on each core            
            element = file_gen_queue.get()
            current_test_run_arr[element.core] = element
    
    

    

        
        #getting the core number which require file earliest        
        current_time = time.time()
        if(None not in current_test_run_arr):
            
            time_to_complete = [ ((current_time - current_test_run_arr[i].start_time) + sum(float(el[config.TIME]) for el in process_list[i][(current_test_run_arr[i].test_number)+1:last_file_gen_arr[i]+1])) for i in range(CORES) ]
            for i in range(CORES):
                if((last_file_gen_arr[i]+1) == total_tests_arr[i]):
                    time_to_complete[i] = max(time_to_complete)+1
                    
            earliest_complete = time_to_complete.index(min(time_to_complete))
        
        else:
            for i in range(CORES):
                if(current_test_run_arr[i] is None):
                    if((last_file_gen_arr[i]+1) == total_tests_arr[i]):
                        continue
                    earliest_complete = i
                    break
        
        if(earliest_complete == -1):
        	return
        
        
        
        
        
        
        #finding the actual name of the random file
        if(process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE] == 'dieharder' and 
           (process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '200' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '201' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '202' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '203')):
            
            
            test_file = f'{TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.N_TUPL]}.bin'
            
        else:
                
            test_file = f'{TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID]}.bin'
        
        
        
        
        
        
        
        
        #calculating file size to be generated
        file_size = min(int(process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SIZE]), MAX_FILE_SIZE)
        
        
        
        
        
        try:
            generator_method(temp_random_file, file_size)   #call user defined generator
        except:
            print('!!!Error in generator function!!!')
            exit(0)
        
        
        
        
        os.system(f'mv {temp_random_file} {test_file}') #changing the name of the file to original name.
        last_file_gen_arr[earliest_complete] = last_file_gen_arr[earliest_complete]+1
        
        time_file_event.set() #setting the event
    
        
    
    #storing time to generate all the files in an iteration
    os.system(f'mkdir -p {RESULT_DEST}/iteration_{iteration_over_tests}/')
    with open(f'{RESULT_DEST}/iteration_{iteration_over_tests}/file_gen_time.txt','w') as fw:
        fw.write(str(time.time()-start_time))
        
        
