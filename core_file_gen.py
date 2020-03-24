import config
import os
import time
from generator import generator_method
from sys import exit
import subprocess

def inorder_random_file_gen(Tests, inorder_file_event, iteration_over_tests):
    
    temp_random_file = f'{config.TEMP_DEST}/temp_random.bin'
    start_time = time.time()
    for test in Tests:
        
        #checking for some special tests in dieharder which are different 
        #in ntuples only and allocating test file name accordingly
        if(test[config.SUITE] == 'dieharder' and 
           (test[config.ID] == '200' 
            or test[config.ID] == '201' 
            or test[config.ID] == '202' 
            or test[config.ID] == '203')):
            
            
            test_file = f'{config.TEMP_DEST}/{test[config.SUITE]}_{test[config.ID]}_{test[config.N_TUPL]}.bin'
            
        else:
                
            test_file = f'{config.TEMP_DEST}/{test[config.SUITE]}_{test[config.ID]}.bin'
                
        file_size = min(int(test[config.SIZE]), config.MAX_FILE_SIZE)   #calculating file size to be generated
        
        try:
            generator_method(temp_random_file, file_size)   #call generator to generate file
        except:
            print('!!!Cannot generate numbers from generator function!!!')
            exit(0)
        
        if('False' in subprocess.run(f'test -e {temp_random_file} && echo True || echo False ', stdout=subprocess.PIPE, shell = True).stdout.decode('utf-8')):
            print('!!!Cannot generate numbers from generator function!!!')
            exit(0)
        os.system(f'mv {temp_random_file} {test_file}')
        
        inorder_file_event.set()
        
    os.system(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration_over_tests}/')
    with open(f'{config.RESULT_DEST}/iteration_{iteration_over_tests}/file_gen_time.txt','w') as fw:
        fw.write(str(time.time()-start_time))


def random_file_gen_time(process_list, file_gen_queue, total_tests_arr, time_file_event, iteration_over_tests):
    
    start_time = time.time()
    total_tests = sum(total_tests_arr)
    earliest_complete = -1
    temp_random_file = f'{config.TEMP_DEST}/temp_random.bin'
    
    current_test_run_arr = [None]*config.CORES      #current test running in the ith core
    
    
    last_file_gen_arr = []      #last file generated in a core for nth test
    for i in range(config.CORES):
        last_file_gen_arr.append(-1)
        
    while((sum(last_file_gen_arr)+config.CORES) < total_tests):      #+1 for array starts from 0
        
        
        while(file_gen_queue.empty() is False):     #getting the current test running on each core
            
            element = file_gen_queue.get()
            current_test_run_arr[element.core] = element
    
        current_time = time.time()      
        
        #getting the core no which require file earliest        
        if(None not in current_test_run_arr):
            
            time_to_complete = [ ((current_time - current_test_run_arr[i].start_time) + sum(float(el[config.TIME]) for el in process_list[i][(current_test_run_arr[i].test_number)+1:last_file_gen_arr[i]+1])) for i in range(config.CORES) ]
            for i in range(config.CORES):
                if((last_file_gen_arr[i]+1) == total_tests_arr[i]):
                    time_to_complete[i] = max(time_to_complete)+1
                    
            earliest_complete = time_to_complete.index(min(time_to_complete))
        
        else:
            for i in range(config.CORES):
                if(current_test_run_arr[i] is None):
                    if((last_file_gen_arr[i]+1) == total_tests_arr[i]):
                        continue
                    earliest_complete = i
                    break
        
        if(earliest_complete == -1):
        	return
        #checking for some special tests in dieharder which are different 
        #in ntuples only and allocating test file name accordingly
        if(process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE] == 'dieharder' and 
           (process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '200' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '201' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '202' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID] == '203')):
            
            
            test_file = f'{config.TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.N_TUPL]}.bin'
            
        else:
                
            test_file = f'{config.TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.ID]}.bin'
    
        #calculating file size to be generated
        file_size = min(int(process_list[earliest_complete][last_file_gen_arr[earliest_complete]+1][config.SIZE]), config.MAX_FILE_SIZE)
        
        try:
            generator_method(temp_random_file, file_size)   #call generator to generate file
        except:
            print('!!!Error in generator function!!!')
            exit(0)
        
        os.system(f'mv {temp_random_file} {test_file}')
        last_file_gen_arr[earliest_complete] = last_file_gen_arr[earliest_complete]+1
        
        time_file_event.set()
        
    os.system(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration_over_tests}/')
    with open(f'{config.RESULT_DEST}/iteration_{iteration_over_tests}/file_gen_time.txt','w') as fw:
        fw.write(str(time.time()-start_time))
        
        
