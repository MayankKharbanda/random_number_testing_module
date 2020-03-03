import multiprocessing
import os
import time
from process_allocation_algo import process_alloc
import config
from test_reader import test_reader


#contains start time of running of the whole module
module_start_time = time.time()



Tests = test_reader(config.TESTS_FILE)    #contains the list of all the 
                                            #tests to run on random number generator.



file_seek = 0   #contains location in the random source from 
                #where the numbers are taken. 

with open(config.RANDOM_SOURCE,'r') as fr:
    fr.seek(0,2)
    SOURCE_FILE_SIZE = fr.tell()



#TODO add print statements for error




'''
The function runs individually for each core,
and executes the test on the random numbers.
'''

def process(param, global_e, local_e, test_file):
    
    
    '''
    input: param: test to execute
            global_e: global event, which is unique for all the cores.
            local_e: local event, for every individual core.
            test_file: binary file containing random data, on which 
                    test is executed.
    
    output: results of tests at result destination.
            Time taken to execute the test.
    '''
    
    
    process_start_time = time.time()        #contains the initial time of the test executing.
    
    
    
    '''
    checks the suite of the test, and execute the commands accordingly.
    '''
    
    if(param[config.SUITE]=='smallcrush'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/small_crush/')
        os.system(f'Tests/testu01 -m small_crush -i {test_file} -t {param[config.ID]} > {config.RESULT_DEST}/small_crush/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='crush'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/crush/')
        os.system(f'Tests/testu01 -m crush -i {test_file} -t {param[config.ID]} > {config.RESULT_DEST}/crush/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='bigcrush'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/big_crush/')
        os.system(f'Tests/testu01 -m big_crush -i {test_file} -t {param[config.ID]} > {config.RESULT_DEST}/big_crush/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='alphabit'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/alphabit/')
        os.system(f'Tests/testu01 -m alphabit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]} > {config.RESULT_DEST}/alphabit/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='rabbit'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/rabbit/')
        os.system(f'Tests/testu01 -m rabbit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]} > {config.RESULT_DEST}/rabbit/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/dieharder/')
        os.system(f'Tests/dieharder -d {param[config.ID]} -n {param[config.N_TUPL]} -f {test_file} -g 201 > {config.RESULT_DEST}/dieharder/{param[config.ID]}_{param[config.N_TUPL]}.txt')
    
    
    elif(param[config.SUITE]=='dieharder'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/dieharder/')
        os.system(f'Tests/dieharder -d {param[config.ID]} -f {test_file} -g 201 > {config.RESULT_DEST}/dieharder/{param[config.ID]}.txt')
    
    
    elif(param[config.SUITE]=='nist'):
        
        os.system(f'mkdir -p {config.RESULT_DEST}/nist/{param[config.ID]}/{param[config.NAME]}/')
        os.system(f'Tests/nist {param[config.ID]} {test_file} {config.RESULT_DEST}/nist/{param[config.ID]} {param[config.SIZE]}')

    
    
    
    os.system(f'rm {test_file}')    #remove the random file created for the test.
    
    process_end_time = time.time()  #contains end time of the test.
    


    process_time = process_end_time - process_start_time    #time to execute the test.
    
    if(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        
        with open(f'{config.RESULT_DEST}/{param[config.SUITE]}_{param[config.ID]}_{param[config.N_TUPL]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    else:
        
        with open(f'{config.RESULT_DEST}/{param[config.SUITE]}_{param[config.ID]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    
    
    local_e.set()
    global_e.set()    #setting events




os.system(f'mkdir -p {config.TEMP_DEST}/')  #directory creation for random files



#summation of tests in all cores
total_tests_all = len(Tests)





tests_completed = 0    #total tests completed till this moment.
total_wait_time = 0     #total wait time for random number generator.





#events for, each process, if completed execution or not
process_event = []
for i in range(config.CORES):
    process_event.append(multiprocessing.Event())
    process_event[i].set()




#global event 
process_event_global = multiprocessing.Event()
process_event_global.set()




#variable for each core running
process_arr = [None]*config.CORES



#array contaning n-lists of tests, each for a particular core according 
#to time to execute.
process_list = process_alloc(config.CORES, Tests)




#check if test execution time is there.
if(process_list!=-1):
    
    
    #array of number of tests in a particular core
    total_tests_each_p = []


    for i in range(config.CORES):
        total_tests_each_p.append(len(process_list[i]))


    
    #contains the number of tests completed in a core
    test_process = []
    for i in range(config.CORES):
        test_process.append(0)
    

    
    while tests_completed < total_tests_all:
        
        
        #random number generator wait time calculation
        start_time = time.time()
        process_event_global.wait()
        end_time = time.time()
        
        
        total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
        
        #checking each core to find which core generated event.
        for i in range(config.CORES):
        
            if(process_event[i].is_set() and test_process[i] < total_tests_each_p[i]):
                
                
                #checking for some special tests in dieharder which are different 
                #in ntuples only and allocating test file name accordingly
                if(process_list[i][test_process[i]][config.SUITE] == 'dieharder' and 
                   (process_list[i][test_process[i]][config.ID] == '200' 
                    or process_list[i][test_process[i]][config.ID] == '201' 
                    or process_list[i][test_process[i]][config.ID] == '202' 
                    or process_list[i][test_process[i]][config.ID] == '203')):
                    
                    
                    test_file = f'{config.TEMP_DEST}/{process_list[i][test_process[i]][config.SUITE]}_{process_list[i][test_process[i]][config.NAME]}_{process_list[i][test_process[i]][config.ID]}_{process_list[i][test_process[i]][config.N_TUPL]}.bin'
                
                else:
                    
                    test_file = f'{config.TEMP_DEST}/{process_list[i][test_process[i]][config.SUITE]}_{process_list[i][test_process[i]][config.NAME]}_{process_list[i][test_process[i]][config.ID]}.bin'
                
                
                #random bin file creation for the test
                with open(config.RANDOM_SOURCE,'rb') as rf, open(test_file,'wb') as wf:
                    
                    file_size = min(int(Tests[tests_completed][config.SIZE]), config.MAX_FILE_SIZE)

                    if(file_seek + file_size > SOURCE_FILE_SIZE):
                        file_seek = 0
                    
                    wf.seek(file_seek, 0)
                    wf.write(rf.read(file_size))
                    file_seek = file_seek + file_size
                
                
                print(f'Running test {process_list[i][test_process[i]][config.NAME]} in core {i}')
                
                #allocation of test to the core
                process_arr[i] = multiprocessing.Process(target=process, args=(process_list[i][test_process[i]], process_event_global, process_event[i], test_file))
                process_arr[i].start()
            
                
                test_process[i] = test_process[i] + 1
                tests_completed = tests_completed + 1
                
                #resetting local event
                process_event[i].clear()
            
    
        #resetting global event
        process_event_global.clear()



else:
    
    while tests_completed < total_tests_all:
        
        
        #random number generator wait time calculation
        start_time = time.time()
        process_event_global.wait()
        end_time = time.time()
        
        total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
        
        #checking each core to find which core generated event.
        for i in range(config.CORES):
        
            if(process_event[i].is_set() and tests_completed < total_tests_all):
                
                
                #checking for some special tests in dieharder which are different 
                #in ntuples only and allocating test file name accordingly
                if(Tests[tests_completed][config.SUITE] == 'dieharder' and 
                   (Tests[tests_completed][config.ID] == '200' 
                    or Tests[tests_completed][config.ID] == '201' 
                    or Tests[tests_completed][config.ID] == '202' 
                    or Tests[tests_completed][config.ID] == '203')):
                    
                    
                    test_file = f'{config.TEMP_DEST}/{Tests[tests_completed][config.SUITE]}_{Tests[tests_completed][config.NAME]}_{Tests[tests_completed][config.ID]}_{Tests[tests_completed][config.N_TUPL]}.bin'
                
                else:
                    
                    test_file = f'{config.TEMP_DEST}/{Tests[tests_completed][config.SUITE]}_{Tests[tests_completed][config.NAME]}_{Tests[tests_completed][config.ID]}.bin'
                
                
                #random bin file creation for the test
                with open(config.RANDOM_SOURCE,'rb') as rf, open(test_file,'wb') as wf:
                    
                    file_size = min(int(Tests[tests_completed][config.SIZE]), config.MAX_FILE_SIZE)
                    
                    if(file_seek + file_size > SOURCE_FILE_SIZE):
                        file_seek = 0
                    
                    wf.seek(file_seek, 0)
                    wf.write(rf.read(file_size))
                    file_seek = file_seek + file_size
                
                
                print(f'Running test {Tests[tests_completed][config.NAME]} in core {i}')
                
                
                #allocation of test to the core
                process_arr[i] = multiprocessing.Process(target=process, args=(Tests[tests_completed], process_event_global, process_event[i], test_file))
                process_arr[i].start()
                
                
                tests_completed = tests_completed + 1
                
                #resetting local event
                process_event[i].clear()
            
    
        #resetting global event
        process_event_global.clear()





#waiting for each core to complete execution, after running all tests
for i in range(config.CORES):
    process_event[i].wait()



#remove the temp directory
os.system(f'rm -r {config.TEMP_DEST}/')



#Writing all the details to output file
for Test in Tests:
    
    if(Test[config.SUITE]=='dieharder' and 
         (Test[config.ID] == '200' 
          or Test[config.ID] == '201' 
          or Test[config.ID] == '202' 
          or Test[config.ID] == '203')):
        
        with open(f'{config.RESULT_DEST}/{Test[config.SUITE]}_{Test[config.ID]}_{Test[config.N_TUPL]}_time.txt','w') as fr:
            Test[config.TIME] = str(round(float((fr.readline()).strip()),2))
        os.system(f'rm {config.RESULT_DEST}/{Test[config.SUITE]}_{Test[config.ID]}_{Test[config.N_TUPL]}_time.txt')
    else:
        with open(f'{config.RESULT_DEST}/{Test[config.SUITE]}_{Test[config.ID]}_time.txt','r') as fr:
            Test[config.TIME] = str(round(float((fr.readline()).strip()),2))
        os.system(f'rm {config.RESULT_DEST}/{Test[config.SUITE]}_{Test[config.ID]}_time.txt')



module_end_time = time.time()
module_running_time = module_end_time - module_start_time



#storing the wait time into file
with open(f'{config.RESULT_DEST}/wait_time.txt','w') as fw:
    fw.write("Total_wait_time (in s) :"+str(total_wait_time)+"\n")
    fw.write("Module running time (in s) :"+str(module_running_time)+"\n")
    fw.write('SNO'.rjust(3))
    fw.write('SUITE'.rjust(15))
    fw.write('NAME'.rjust(30))
    fw.write('ID'.rjust(3))
    fw.write('TIME'.rjust(10))
    fw.write('SIZE'.rjust(15))
    fw.write('N_TUPLE'.rjust(10))
    fw.write("\n")
    for Test in range(len(Tests)):
        fw.write(Tests[Test][config.SNO].rjust(3))
        fw.write(Tests[Test][config.SUITE].rjust(15))
        fw.write(Tests[Test][config.NAME].rjust(30))
        fw.write(Tests[Test][config.ID].rjust(3))
        fw.write(Tests[Test][config.TIME].rjust(10))
        fw.write(Tests[Test][config.SIZE].rjust(15))
        if(len(Tests[Test]) == config.N_TUPL+1):
            fw.write(Tests[Test][config.N_TUPL].rjust(10))
        fw.write("\n")
