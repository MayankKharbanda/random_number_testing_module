import multiprocessing
import os
import time
from process_allocation_algo import process_alloc



#function to call the test file, containing all the tests
def process(param, global_e, local_e):
    os.system(f'byte_stream/tests.sh {param}')
    local_e.set()
    global_e.set()    #setting event



cores = 3

#array contaning n-lists of tests each for a particular core
process_list = process_alloc(cores)


#array of number of tests in a particular core
total_tests_each_p = []

for i in range(cores):
    total_tests_each_p.append(len(process_list[i]))


#summation of tests in all cores
total_tests_all = sum(total_tests_each_p)


#contains the value n+1 if n tests are completed in a core
test_process = []
for i in range(cores):
    test_process.append(1)
    


tests_completed = 0    #total tests completed till this moment
total_wait_time = 0


#event for, each process, if completed execution or not
process_event = []
for i in range(cores):
    process_event.append(multiprocessing.Event())
    process_event[i].set()

#global event 
process_event_global = multiprocessing.Event()
process_event_global.set()



#variable for each core running
process_arr = [None]*cores




while tests_completed < total_tests_all:
    
    
    #wait time calculation
    start_time = time.time()
    process_event_global.wait()
    end_time = time.time()
    
    total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
    #checking each core if completed execution or not
    for i in range(cores):
        
        if(process_event[i].is_set() and test_process[i] <= total_tests_each_p[i]):
            
            process_arr[i] = multiprocessing.Process(target=process, args=(test_process[i], process_event_global, process_event[i]))
            process_arr[i].start()
            
            test_process[i] = test_process[i] + 1
            tests_completed = tests_completed + 1
            #resetting local event
            process_event[i].clear()
    
    
    #resetting global event
    process_event_global.clear()
    
   
#waiting for each core to complete
for i in range(cores):
    process_event[i].wait()
    

#storing the wait time into file
with open('results_parallel_process/wait_time.txt','w') as f:
    f.write("Total_wait_time (in s) :"+str(total_wait_time))