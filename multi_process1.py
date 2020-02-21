import multiprocessing
import os
import time
from process_allocation_algo import process_alloc
from config import config

SNO = 0
SUITE = 1
NAME = 2
ID = 3
TIME = 4
SIZE = 5

module_start_time = time.time()

Tests = config('config3.txt')
random_source = 'random_numbers_time/dieharder203.bin'
result_dest = 'results_parallel_process'

cores = 4


os.system(f'mkdir -p results_parallel_process/')

#function to call the test file, containing all the tests
def process(param, global_e, local_e):
    process_start_time = time.time()
    
    if(param[SUITE]=='smallcrush'):
        os.system(f'Tests/testu01 -m small_crush -i {random_source} -t {param[ID]} >> {result_dest}/small_crush_{param[ID]}.txt')
    elif(param[SUITE]=='crush'):
        os.system(f'Tests/testu01 -m crush -i {random_source} -t {param[ID]} >> {result_dest}/crush_{param[ID]}.txt')
    elif(param[SUITE]=='bigcrush'):
        os.system(f'Tests/testu01 -m big_crush -i {random_source} -t {param[ID]} >> {result_dest}/big_crush_{param[ID]}.txt')
    elif(param[SUITE]=='dieharder'):
        os.system(f'Tests/dieharder -d {param[ID]} -f {random_source} -g 201 > {result_dest}/dieharder_{param[ID]}.txt')
    elif(param[SUITE]=='nist'):
        os.system(f'mkdir -p results_parallel_process/{param[ID]}/{param[NAME]}/')
        os.system(f'Tests/nist {param[ID]}')
    else:
        print("Wrong Test Names")
    
    process_end_time = time.time()
    
    process_time = process_end_time - process_start_time
    with open(f'{result_dest}/{param[SUITE]}_{param[ID]}_time.txt','w') as fw:
        fw.write(str(process_time))
    
    local_e.set()
    global_e.set()    #setting event



#summation of tests in all cores
total_tests_all = len(Tests)

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


#array contaning n-lists of tests each for a particular core
process_list = process_alloc(cores, Tests)


if(process_list!=-1):
    #array of number of tests in a particular core
    total_tests_each_p = []


    for i in range(cores):
        total_tests_each_p.append(len(process_list[i]))


    #contains the number of tests completed in a core
    test_process = []
    for i in range(cores):
        test_process.append(0)
    

    while tests_completed < total_tests_all:
        
        #wait time calculation
        start_time = time.time()
        process_event_global.wait()
        end_time = time.time()
        
        total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
        #checking each core if completed execution or not
        for i in range(cores):
        
            if(process_event[i].is_set() and test_process[i] < total_tests_each_p[i]):
                #TODO:add test parameters in print statement in next line
                print(f'Running test number {process_list[i][test_process[i]][NAME]} in core {i}')
                process_arr[i] = multiprocessing.Process(target=process, args=(process_list[i][test_process[i]], process_event_global, process_event[i]))
                process_arr[i].start()
            
                test_process[i] = test_process[i] + 1
                tests_completed = tests_completed + 1
                #resetting local event
                process_event[i].clear()
            
    
        #resetting global event
        process_event_global.clear()

else:
    while tests_completed < total_tests_all:
        
        #wait time calculation
        start_time = time.time()
        process_event_global.wait()
        end_time = time.time()
        
        total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
        #checking each core if completed execution or not
        for i in range(cores):
        
            if(process_event[i].is_set()):
                #TODO: update print here also
                print(f'Running test number {Tests[tests_completed][NAME]} in core {i}')
                process_arr[i] = multiprocessing.Process(target=process, args=(Tests[tests_completed], process_event_global, process_event[i]))
                process_arr[i].start()
            
                tests_completed = tests_completed + 1
                #resetting local event
                process_event[i].clear()
            
    
        #resetting global event
        process_event_global.clear()
   
#waiting for each core to complete
for i in range(cores):
    process_event[i].wait()

for Test in Tests:
    with open(f'{result_dest}/{Test[SUITE]}_{Test[ID]}_time.txt','r') as fr:
        Test[TIME] = str(round(float((fr.readline()).strip()),2))
    os.system(f'rm {result_dest}/{Test[SUITE]}_{Test[ID]}_time.txt')

module_end_time = time.time()
module_running_time = module_end_time - module_start_time
#storing the wait time into file
with open(f'{result_dest}/wait_time.txt','w') as fw:
    fw.write("Total_wait_time (in s) :"+str(total_wait_time)+"\n")
    fw.write("Module running time (in s) :"+str(module_running_time)+"\n")
    fw.write('SNO'.rjust(3))
    fw.write('SUITE'.rjust(15))
    fw.write('NAME'.rjust(30))
    fw.write('ID'.rjust(3))
    fw.write('TIME'.rjust(5))
    fw.write('SIZE'.rjust(15))
    fw.write("\n")
    for Test in range(len(Tests)):
        fw.write(Tests[Test][SNO].rjust(3))
        fw.write(Tests[Test][SUITE].rjust(15))
        fw.write(Tests[Test][NAME].rjust(30))
        fw.write(Tests[Test][ID].rjust(3))
        fw.write(Tests[Test][TIME].rjust(5))
        fw.write(Tests[Test][SIZE].rjust(15))
        fw.write("\n")