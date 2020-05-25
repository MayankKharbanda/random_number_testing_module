import multiprocessing
import os
import time
from process_allocation_algo import process_alloc
import config
from test_reader import test_reader
from signal import signal, SIGINT
import sys
import subprocess
from core_function import process
from core_file_gen import inorder_random_file_gen, random_file_gen_time
from file_gen_class import File_gen
from config_arg import parse_arg









#arguments parsing
ARGS = parse_arg()
NUMBER_OF_ITERATIONS = ARGS.iteration
RESULT_DEST = ARGS.dest_loc
CORES = ARGS.cores - 1
TEMP_DEST = ARGS.temp_dest
MAX_FILE_SIZE = ARGS.max_size










def exit_func(signal_received, frame):  
    
    '''
    the function handles exit from module.
    '''
    
    
    
    print('SIGINT or CTRL-C detected.')
    
    
    
    
    #remove the temp directory
    os.system(f'rm -rf {TEMP_DEST}/')


    module_end_time = time.time()       #evaluating module running time and storing it
    module_running_time = module_end_time - module_start_time

    with open(f'{RESULT_DEST}/module_report.txt','w') as fw:
        fw.write("Module running time (in s) :"+str(module_running_time)+"\n")
        
    print('EXITING...')
    
    sys.exit(0)












file_gen_queue = multiprocessing.Queue()    #queue used for current test running in a core

module_start_time = time.time()

Tests = test_reader(ARGS.tests_file)    #contains the list of all the tests to run on random number generator.

os.system(f'mkdir -p {TEMP_DEST}/')  #directory for random files

#Total tests in test file
total_tests_all = len(Tests)








#local events for each process
process_event = []
for i in range(CORES):
    process_event.append(multiprocessing.Event())
    process_event[i].set()


#global event
process_event_global = multiprocessing.Event()
process_event_global.set()








#variable for each process running
process_arr = [None]*CORES
random_file_gen_process = None  #file generation process
iteration_over_tests = 0    #iteration over the test file







signal(SIGINT, exit_func)   #initialization of signal to handle exit from module













while(True):        #infinite loop over test-file

    



    tests_completed = 0    #total tests completed till this moment.
    total_wait_time = 0     #total wait time for the main module.




    #exit from loop
    if(iteration_over_tests == int(NUMBER_OF_ITERATIONS)):
        exit_func(None, None)
    
    
    iteration_over_tests = iteration_over_tests + 1
    
    
    
    
    
    
    #array contaning n-lists of tests, each for a particular core according 
    #to time to execute.
    process_list = process_alloc(Tests, CORES)






    #check if test execution time exists.
    if(process_list!=-1):

        
        time_file_event = multiprocessing.Event()   #event for file generation
        time_file_event.clear()
        
        #array of number of tests in a particular core
        total_tests_arr = []

        for i in range(CORES):
            total_tests_arr.append(len(process_list[i]))



        random_file_gen_process = multiprocessing.Process(target=random_file_gen_time, args=(process_list, file_gen_queue, total_tests_arr, time_file_event, iteration_over_tests, RESULT_DEST, CORES, TEMP_DEST, MAX_FILE_SIZE))
        random_file_gen_process.start()        #start the process to generate random number file
    

        
        #contains the number of tests allocated on a core
        process_comleted_arr = []
        for i in range(CORES):
            process_comleted_arr.append(0)
    

        while tests_completed < total_tests_all:
                                    
            #wait time calculation
            start_time = time.time()
            process_event_global.wait()
            end_time = time.time()
            
            #resetting global event
            process_event_global.clear()                
            total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
        
            #checking each core to find which generated event.
            for i in range(CORES):
        
                if(process_event[i].is_set() and process_comleted_arr[i] < total_tests_arr[i]):
                
                    #resetting local event
                    process_event[i].clear()
                    
                    #creating test file name
                    if(process_list[i][process_comleted_arr[i]][config.SUITE] == 'dieharder' and 
                       (process_list[i][process_comleted_arr[i]][config.ID] == '200' 
                        or process_list[i][process_comleted_arr[i]][config.ID] == '201' 
                        or process_list[i][process_comleted_arr[i]][config.ID] == '202' 
                        or process_list[i][process_comleted_arr[i]][config.ID] == '203')):
                    
                        test_file = f'{TEMP_DEST}/{process_list[i][process_comleted_arr[i]][config.SUITE]}_{process_list[i][process_comleted_arr[i]][config.ID]}_{process_list[i][process_comleted_arr[i]][config.N_TUPL]}.bin'
                
                    else:
                        test_file = f'{TEMP_DEST}/{process_list[i][process_comleted_arr[i]][config.SUITE]}_{process_list[i][process_comleted_arr[i]][config.ID]}.bin'
                
                    
                
                
                
                    #waiting for required file
                    FILE_EXIST = 'False'    
                    while( 'True' not in FILE_EXIST ):        
                        out = subprocess.run(f'test -e {test_file} && echo True || echo False ', stdout=subprocess.PIPE, shell = True)
                        FILE_EXIST = out.stdout.decode('utf-8')
                        if('True' not in FILE_EXIST):
                            time_file_event.wait()
                            time_file_event.clear()

                    
                    
                    
                    
                    process_start_time = time.time()        #contains the start time of the test executing.
                    #starting the process
                    process_arr[i] = multiprocessing.Process(target=process, args=(process_list[i][process_comleted_arr[i]], process_event_global, process_event[i], test_file, iteration_over_tests, process_start_time, i, RESULT_DEST))
                    
                    try:
                        process_arr[i].start()
                    except:
                        print('!!!Error in process core {i}, test {process_list[i][process_comleted_arr[i]]}, exiting')
                        sys.exit(0)
                        


                        
                    #the info of which test is running on the core
                    file_gen_queue.put(File_gen(start_time=process_start_time,
                                                core=i, test_number=process_comleted_arr[i]))
                    

                    process_comleted_arr[i] = process_comleted_arr[i] + 1
                    tests_completed = tests_completed + 1
        
        while(file_gen_queue.empty() is False):     #Cleaning the queue after the iteration
            file_gen_queue.get()
                
            






    else:
        
        inorder_file_event = multiprocessing.Event()    #event for file generation
        inorder_file_event.clear()        
        random_file_gen_process = multiprocessing.Process(target=inorder_random_file_gen, args=(Tests, inorder_file_event, iteration_over_tests, RESULT_DEST, TEMP_DEST, MAX_FILE_SIZE))
        random_file_gen_process.start()     #start the process to generate random number file
        
        
        
        
        
        while tests_completed < total_tests_all:
        
            #wait time calculation
            start_time = time.time()
            process_event_global.wait()
            end_time = time.time()
        
            #resetting global event
            process_event_global.clear()
            total_wait_time = total_wait_time + (end_time - start_time)
    
    
    
    
        
            #checking each core to find which generated event.
            for i in range(CORES):
      
                
                if(process_event[i].is_set() and tests_completed < total_tests_all):
                    
                    #resetting local event
                    process_event[i].clear()
                    
                    #creating test file name
                    if(Tests[tests_completed][config.SUITE] == 'dieharder' and 
                       (Tests[tests_completed][config.ID] == '200' 
                        or Tests[tests_completed][config.ID] == '201' 
                        or Tests[tests_completed][config.ID] == '202' 
                        or Tests[tests_completed][config.ID] == '203')):
            
            
                        test_file = f'{TEMP_DEST}/{Tests[tests_completed][config.SUITE]}_{Tests[tests_completed][config.ID]}_{Tests[tests_completed][config.N_TUPL]}.bin'
            
                    else:
                
                        test_file = f'{config.TEMP_DEST}/{Tests[tests_completed][config.SUITE]}_{Tests[tests_completed][config.ID]}.bin'
                    
                    
                    
                    
                    
                    #waiting for required file
                    FILE_EXIST = 'False'
                    while( 'True' not in FILE_EXIST ):    
                        inorder_file_event.clear()    
                        if(not random_file_gen_process.is_alive()):     #check if file generation is in process or not.
                            out = subprocess.run(f'test -e {test_file} && echo True || echo False ', stdout=subprocess.PIPE, shell = True)
                            FILE_EXIST = out.stdout.decode('utf-8')        
                            if('True' not in FILE_EXIST):
                                print(f'\nFile with random numbers for test {Tests[tests_completed][config.SUITE]}, {Tests[tests_completed][config.ID]} doesn\'t exist \nand the core_file_gen process doesn\'t exist. ')
                                exit_func(None, None)    
                        else:
                            out = subprocess.run(f'test -e {test_file} && echo True || echo False ', stdout=subprocess.PIPE, shell = True)
                            FILE_EXIST = out.stdout.decode('utf-8')     
                        if('True' not in FILE_EXIST):
                            inorder_file_event.wait()
                                

                    

                    process_start_time = time.time()        #contains the start time of the test executing.
                    #starting the process
                    process_arr[i] = multiprocessing.Process(target=process, args=(Tests[tests_completed], process_event_global, process_event[i], test_file, iteration_over_tests, process_start_time, i, RESULT_DEST))
                    
                    try:
                        process_arr[i].start()
                    except:
                        print('!!!Error in process core {i}, test {Tests[tests_completed]}, exiting')
                        sys.exit(0)
                
                
                    tests_completed = tests_completed + 1
                
                
            









    #waiting for each core to complete execution
    for i in range(CORES):
        process_event[i].wait()




    #Writing all the details to output file
    for Test in Tests:    
        if(Test[config.SUITE]=='dieharder' and 
           (Test[config.ID] == '200' 
            or Test[config.ID] == '201' 
            or Test[config.ID] == '202' 
            or Test[config.ID] == '203')):
            
            
            with open(f'{RESULT_DEST}/iteration_{iteration_over_tests}/{Test[config.SUITE]}_{Test[config.ID]}_{Test[config.N_TUPL]}_time.txt','r') as fr:
                Test[config.TIME] = str(round(float((fr.readline()).strip()),2))
            os.system(f'rm {RESULT_DEST}/iteration_{iteration_over_tests}/{Test[config.SUITE]}_{Test[config.ID]}_{Test[config.N_TUPL]}_time.txt')
        else:
            with open(f'{RESULT_DEST}/iteration_{iteration_over_tests}/{Test[config.SUITE]}_{Test[config.ID]}_time.txt','r') as fr:
                Test[config.TIME] = str(round(float((fr.readline()).strip()),2))
            os.system(f'rm {RESULT_DEST}/iteration_{iteration_over_tests}/{Test[config.SUITE]}_{Test[config.ID]}_time.txt')






    #storing the wait time into file
    with open(f'{RESULT_DEST}/iteration_{iteration_over_tests}/final_report.txt','w') as fw:
        fw.write("Total_wait_time (in s) :"+str(total_wait_time)+"\n")
        fw.write('SUITE'.rjust(15))
        fw.write('NAME'.rjust(30))
        fw.write('ID'.rjust(3))
        fw.write('TIME'.rjust(10))
        fw.write('SIZE'.rjust(15))
        fw.write('N_TUPLE'.rjust(10))
        fw.write("\n")
        for Test in range(len(Tests)):
            fw.write(Tests[Test][config.SUITE].rjust(15))
            fw.write(Tests[Test][config.NAME].rjust(30))
            fw.write(Tests[Test][config.ID].rjust(3))
            fw.write(Tests[Test][config.TIME].rjust(10))
            fw.write(Tests[Test][config.SIZE].rjust(15))
            if(len(Tests[Test]) == config.N_TUPL+1):
                fw.write(Tests[Test][config.N_TUPL].rjust(10))
            fw.write("\n")
    
