import numpy as np

def process_alloc(cores):
    test_time = []         #list of tests with their time to execute
    process_list = []       #final list of tests on each processes


    with open('byte_stream/test_time.txt','r') as tt:
        for line in tt.readlines():
            test_time.append([int(line.split()[0]),int(line.split()[1])])
        

    test_time_copy = test_time.copy()

    #cores = core#number of cores/process lists


    for _ in range(cores):
        process_list.append([])


    #sorting list wrt time to execute
    test_time_copy.sort(key = lambda x:x[1])


    total_time = 0     #summation of wait time of all the processors


    if(len(test_time_copy)>cores):
        total_time = np.sum(test_time_copy[:-cores], 0)[1]


    #wait time for each processor/ time taken to start last test on the process
    approx_time_each_process = total_time/cores


    #adding last test to each process
    for i in range(cores):
        if(len(test_time_copy)>0):
            process_list[-(i+1)].insert(0, test_time_copy[-1])
            del test_time_copy[-1]



    #adding tests to all the processes except the first one
    for i in range(cores-1):
        if(len(test_time_copy)>0):
            temp_sum = test_time_copy[-1][1]
            process_list[-(i+1)].insert(0, test_time_copy[-1])
            del test_time_copy[-1]
            if(len(test_time_copy)>0):
                temp_sum = temp_sum+test_time_copy[0][1]
                j = 0
                while(temp_sum < approx_time_each_process):
                    process_list[-(i+1)].insert(j, test_time_copy[0])
                    del test_time_copy[0]
                    j = j+1
                    if(len(test_time_copy) == 0):
                        break
                    temp_sum = temp_sum+test_time_copy[0][1]


    #adding all left over tests to the first processor
    j=0
    while(len(test_time_copy)!=0):
        process_list[0].insert(j,test_time_copy[0])
        j = j+1
        del test_time_copy[0]
    
    return process_list