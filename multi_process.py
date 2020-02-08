import multiprocessing
import os
import time



#process includes fast tests
def process1(param, global_e, local_e):
    os.system(f'byte_stream/fast.sh {param}')
    local_e.set()
    global_e.set()    #setting event


#process includes normal tests
def process2(param, global_e, local_e):
    os.system(f'byte_stream/normal.sh {param}')
    local_e.set()
    global_e.set()   #setting event



#total tests in a particular process and summation of those
total_test_process_1 = 5
total_test_process_2 = 5
total_tests = 10


#initial conditions
test_process_1 = 1
test_process_2 = 1
tests_completed = 0
total_wait_time = 0


#event added if any process has completed execution or not
process_event_1 = multiprocessing.Event()
process_event_2 = multiprocessing.Event()
process_event_global = multiprocessing.Event()
process_event_1.set()
process_event_2.set()
process_event_global.set()



while tests_completed < total_tests:
    
    #wait time calculation
    start_time = time.time()
    process_event_global.wait()
    end_time = time.time()
    
    total_wait_time = total_wait_time + (end_time - start_time)
    
    #starting process1
    if(process_event_1.is_set() and test_process_1 <= total_test_process_1):
        process_1 = multiprocessing.Process(target=process1, args=(test_process_1, process_event_global, process_event_1))
        process_1.start()
        test_process_1 = test_process_1 + 1
        tests_completed = tests_completed + 1
        process_event_1.clear()
    
    
    #starting process2
    if(process_event_2.is_set() and test_process_2 <= total_test_process_2):
        process_2 = multiprocessing.Process(target=process2, args=(test_process_2, process_event_global, process_event_2))
        process_2.start()
        tests_completed = tests_completed + 1
        test_process_2 = test_process_2 + 1
        process_event_2.clear()
    
    #resetting event
    process_event_global.clear()
    
    
with open('results_parallel_process/wait_time.txt','w') as f:
    f.write("Total_wait_time (in s) :"+str(total_wait_time))