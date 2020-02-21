
SNO = 0
SUITE = 1
NAME = 2
ID = 3
TIME = 4
SIZE = 5


def process_alloc(cores, Tests):
    
    #checking for running time
    for test in range(len(Tests)):
        if(Tests[test][TIME]=='None'):
            return -1
                

    process_list = []       #final list of tests on each processes

    tests_copy = Tests.copy()


    for _ in range(cores):
        process_list.append([])


    #sorting list wrt time to execute
    tests_copy.sort(key = lambda x:int(x[TIME]))


    total_time = 0     #summation of wait time of all the processors


    if(len(tests_copy)>cores):
        total_time = sum(int(test[TIME]) for test in tests_copy[:-cores])


    #wait time for each processor/ time taken to start last test on the process
    approx_time_each_process = total_time/cores


    #adding last test to each process
    for i in range(cores):
        if(len(tests_copy)>0):
            process_list[-(i+1)].insert(0, tests_copy[-1])
            del tests_copy[-1]



    #adding tests to all the processes except the first one
    for i in range(cores-1):
        if(len(tests_copy)>0):
            temp_sum = int(tests_copy[-1][TIME])
            process_list[-(i+1)].insert(0, tests_copy[-1])
            del tests_copy[-1]
            if(len(tests_copy)>0):
                temp_sum = temp_sum+int(tests_copy[0][TIME])
                j = 0
                while(temp_sum < approx_time_each_process):
                    process_list[-(i+1)].insert(j, tests_copy[0])
                    del tests_copy[0]
                    j = j+1
                    if(len(tests_copy) == 0):
                        break
                    temp_sum = temp_sum+int(tests_copy[0][TIME])


    #adding all left over tests to the first processor
    j=0
    while(len(tests_copy)!=0):
        process_list[0].insert(j,tests_copy[0])
        j = j+1
        del tests_copy[0]
    
    return process_list