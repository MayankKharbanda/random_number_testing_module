import subprocess
import time
import config
import os


'''
The function runs individually for each core,
and executes the test on the random numbers.
'''


def process(param, global_e, local_e, test_file, iteration, process_start_time, core_no):
    
    
    '''
    input: param: test to execute
            global_e: global event, which is unique for all the cores.
            local_e: local event, for every individual core.
            test_file: binary file containing random data, on which 
                    test is executed.
            iteration: iteration value over test file.
    
    output: results of tests at result destination.
            Time taken to execute the test.
    '''
      
    
    '''
    checks the suite of the test, and execute the commands accordingly.
    '''
    
    if(param[config.SUITE]=='smallcrush'):
        
        
        #######################SmallCrush########################################################        
        
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/small_crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m small_crush -i {test_file} -t {param[config.ID]}', stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')
        

        while(output_list[-1] == '' ):  #clean output
            del output_list[-1]

    
        
        if('All tests were passed' in output_list[-1]):
            print(f'\nsmall_crush, {param[config.ID]}, {param[config.NAME]} Passed, iteration_{iteration}, core {core_no}')
        else:
            print(f'\n!!!!ALERT small_crush, {param[config.ID]}, {param[config.NAME]} failed, iteration_{iteration}, core {core_no}')


        
        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/small_crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
    

    
    elif(param[config.SUITE]=='crush'):
        

        #####################################Crush###############################################        
        
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m crush -i {test_file} -t {param[config.ID]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

    
        if('All tests were passed' in output_list[-1]):
            print(f'\ncrush, {param[config.ID]}, {param[config.NAME]} Passed')
        else:
            print(f'\ncrush, {param[config.ID]}, {param[config.NAME]} failed')


        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    elif(param[config.SUITE]=='bigcrush'):
        
        
        ##########################################BigCrush############################################
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/big_crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m big_crush -i {test_file} -t {param[config.ID]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

    
        if('All tests were passed' in output_list[-1]):
            print(f'\nbig_crush, {param[config.ID]}, {param[config.NAME]} Passed')
        else:
            print(f'\nbig_crush, {param[config.ID]}, {param[config.NAME]} failed')


        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/big_crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
                
    
    
    elif(param[config.SUITE]=='alphabit'):
        
        
        #####################################alphabit#################################################
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/alphabit/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m alphabit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

    
        if('All tests were passed' in output_list[-1]):
            print(f'\nalphabit, {param[config.ID]}, {param[config.NAME]} Passed')
        else:
            print(f'\nalphabit, {param[config.ID]}, {param[config.NAME]} failed')


        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/alphabit/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    elif(param[config.SUITE]=='rabbit'):
        
        
        #######################################rabbit#############################################
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/rabbit/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m rabbit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

    
        if('All tests were passed' in output_list[-1]):
            print(f'\nrabbit, {param[config.ID]}, {param[config.NAME]} Passed')
        else:
            print(f'\nrabbit, {param[config.ID]}, {param[config.NAME]} failed')


        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/rabbit/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    elif(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        
        ###############################################dieharder##########################################
        FLAG_DIEHARDER = 1
        
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/dieharder/', shell = True)
        
        out = subprocess.run(f'Tests/dieharder -d {param[config.ID]} -n {param[config.N_TUPL]} -f {test_file} -g 201', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

        for line in output_list[8:]:
            if('PASSED' not in line):
                FLAG_DIEHARDER = 0
        
        
        if(FLAG_DIEHARDER == 0):
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]}, Tuple: {param[config.N_TUPL]} failed')
        else:
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]}, Tuple: {param[config.N_TUPL]} Passed')
    
        
        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/dieharder/{param[config.ID]}_{param[config.N_TUPL]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    elif(param[config.SUITE]=='dieharder'):
        
        
        ###############################################dieharder##########################################
        FLAG_DIEHARDER = 1
        
        
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/dieharder/', shell = True)
        
        out = subprocess.run(f'Tests/dieharder -d {param[config.ID]} -f {test_file} -g 201', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')


        while(output_list[-1] == '' ):    #clean output
            del output_list[-1]

        
        for line in output_list[8:]:
            if('PASSED' not in line):
                FLAG_DIEHARDER = 0
        
        
        if(FLAG_DIEHARDER == 0):
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]} failed')
        else:
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]} Passed')
    
        
        #writing output to result file
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/dieharder/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    elif(param[config.SUITE]=='nist'):
        
        
        ##############################################nist##############################################
        FLAG_NIST = 1
        
        subprocess.run(f'mkdir -p {config.RESULT_DEST}/iteration_{iteration}/nist/{param[config.ID]}/{param[config.NAME]}/', shell = True)
        
        out = subprocess.run(f'Tests/nist {param[config.ID]} {test_file} {config.RESULT_DEST}/iteration_{iteration}/nist/{param[config.ID]} {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split(' ')
        
        
        while("" in output_list):    #clean output 
            output_list.remove("") 
        
        
        for element in output_list[:-1]:
            if(int(element) < int(output_list[-1])):
                FLAG_NIST = 0
        
        
        if(FLAG_NIST == 0):
            print(f'\nnist, {param[config.ID]}, {param[config.NAME]} failed')
        else:
            print(f'\nnist, {param[config.ID]}, {param[config.NAME]} Passed')
    
    
    
    
    os.system(f'rm {test_file}')    #remove the random file created for the test.
    
    process_end_time = time.time()  #contains end time of the test.
    


    process_time = process_end_time - process_start_time    #time to execute the test.
    
    
    #writing time to execute test
    if(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/{param[config.SUITE]}_{param[config.ID]}_{param[config.N_TUPL]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    else:
        
        with open(f'{config.RESULT_DEST}/iteration_{iteration}/{param[config.SUITE]}_{param[config.ID]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    
    
    local_e.set()
    global_e.set()    #setting events