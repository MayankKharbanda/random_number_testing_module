import config
import os
import time

def inorder_random_file_gen(Tests, inorder_file_event):
    
    file_seek = 0   #contains location in the random source from 
                #where the numbers are taken. 

    with open(config.RANDOM_SOURCE,'r') as fr:
        fr.seek(0,2)
        SOURCE_FILE_SIZE = fr.tell()

    temp_random_file = f'{config.TEMP_DEST}/temp_random.bin'
    
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
                
                
        #random bin file creation for the test
        with open(config.RANDOM_SOURCE,'rb') as rf, open(temp_random_file,'wb') as wf:
            
            file_size = min(int(test[config.SIZE]), config.MAX_FILE_SIZE)
                    
            if(file_seek + file_size > SOURCE_FILE_SIZE):
                file_seek = 0
                    
            rf.seek(file_seek, 0)
            wf.write(rf.read(file_size))
            file_seek = file_seek + file_size
            
        os.system(f'mv {temp_random_file} {test_file}')
        inorder_file_event.set()


def random_file_gen_time(process_list, file_gen_queue, total_tests_each_p, time_file_event):
    
    file_seek = 0   #contains location in the random source from 
                #where the numbers are taken. 

    with open(config.RANDOM_SOURCE,'r') as fr:
        fr.seek(0,2)
        SOURCE_FILE_SIZE = fr.tell()
    
    total_tests = sum(total_tests_each_p)
    
    temp_random_file = f'{config.TEMP_DEST}/temp_random.bin'
    
    current_test_run_arr = [None]*config.CORES
    
    
    last_file_gen_arr = []
    for i in range(config.CORES):
        last_file_gen_arr.append(0)
        
    while(sum(last_file_gen_arr) < total_tests):
        
        
        while(file_gen_queue.empty() is False):
            
            element = file_gen_queue.get()
            current_test_run_arr[element.core] = element
    
        current_time = time.time()
        
        if(None not in current_test_run_arr):
            
            time_to_complete = [ ((current_time - current_test_run_arr[i].start_time) + sum(float(el[config.TIME]) for el in process_list[i][(current_test_run_arr[i].test_number)+1:last_file_gen_arr[i]])) for i in range(config.CORES) ]
            for i in range(config.CORES):
                if(last_file_gen_arr[i] == total_tests_each_p[i]):
                    time_to_complete[i] = max(time_to_complete)+1
                    
            earliest_complete = time_to_complete.index(min(time_to_complete))
        
        else:
            for i in range(config.CORES):
                if(current_test_run_arr[i] is None):
                    if(last_file_gen_arr[i] == total_tests_each_p[i]):
                        continue
                    earliest_complete = i
                    break
        #checking for some special tests in dieharder which are different 
        #in ntuples only and allocating test file name accordingly
        if(process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.SUITE] == 'dieharder' and 
           (process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID] == '200' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID] == '201' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID] == '202' 
            or process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID] == '203')):
            
            
            test_file = f'{config.TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.N_TUPL]}.bin'
            
        else:
                
            test_file = f'{config.TEMP_DEST}/{process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.SUITE]}_{process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.ID]}.bin'
    
        #random bin file creation for the test
        with open(config.RANDOM_SOURCE,'rb') as rf, open(temp_random_file,'wb') as wf:
                    
            file_size = min(int(process_list[earliest_complete][last_file_gen_arr[earliest_complete]][config.SIZE]), config.MAX_FILE_SIZE)
            
            if(file_seek + file_size > SOURCE_FILE_SIZE):
                file_seek = 0
                    
            rf.seek(file_seek, 0)
            wf.write(rf.read(file_size))
            file_seek = file_seek + file_size

        os.system(f'mv {temp_random_file} {test_file}')
        last_file_gen_arr[earliest_complete] = last_file_gen_arr[earliest_complete]+1
        
        time_file_event.set()