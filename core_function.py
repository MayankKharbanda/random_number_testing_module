import subprocess
import time
import config
import os




def process(param, global_e, local_e, test_file, iteration, process_start_time, core_no, RESULT_DEST):
    
    
    '''
    

    Parameters
    ----------
    param : test to execute
    global_e : global event for test completion
    local_e : local event for test completion
    test_file : file to be tested
    iteration : iteration on test file
    process_start_time : start time of current test
    core_no : core on which test is running
    RESULT_DEST : destination where result is to be stored
    
    
    

    Returns
    -------
    None.

    '''
    
    
    
    
    
    
    
    if(param[config.SUITE]=='smallcrush'):
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/small_crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m small_crush -i {test_file} -t {param[config.ID]}', stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')
        
        

        while(output_list[-1] == '' ):  #clean output
            del output_list[-1]

    
        
    
        if('All tests were passed' in output_list[-1]):
            print(f'\nsmall_crush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
        else:
            print(f'\n!!! ALERT small_crush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')


        
        #writing output to result file
        with open(f'{RESULT_DEST}/iteration_{iteration}/small_crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
    

    









    elif(param[config.SUITE]=='crush'):
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m crush -i {test_file} -t {param[config.ID]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')



        while(output_list[-1] == '' ):
            del output_list[-1]


    
        if('All tests were passed' in output_list[-1]):
            print(f'\ncrush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
        else:
            print(f'\n!!! ALERT crush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')



        with open(f'{RESULT_DEST}/iteration_{iteration}/crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='bigcrush'):
                
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/big_crush/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m big_crush -i {test_file} -t {param[config.ID]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')




        while(output_list[-1] == '' ):
            del output_list[-1]


    
        if('All tests were passed' in output_list[-1]):
            print(f'\nbig_crush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
        else:
            print(f'\n!!! ALERT big_crush, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')



        with open(f'{RESULT_DEST}/iteration_{iteration}/big_crush/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
                
    
    
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='alphabit'):
                
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/alphabit/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m alphabit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')



        while(output_list[-1] == '' ):
            del output_list[-1]


    
        if('All tests were passed' in output_list[-1]):
            print(f'\nalphabit, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
        else:
            print(f'\n!!! ALERT alphabit, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')



        with open(f'{RESULT_DEST}/iteration_{iteration}/alphabit/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='rabbit'):
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/rabbit/', shell = True)
        
        out = subprocess.run(f'Tests/testu01 -m rabbit -i {test_file} -t {param[config.ID]} --bit_nb {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')



        while(output_list[-1] == '' ):
            del output_list[-1]


    
        if('All tests were passed' in output_list[-1]):
            print(f'\nrabbit, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
        else:
            print(f'\n!!! ALERT rabbit, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')



        with open(f'{RESULT_DEST}/iteration_{iteration}/rabbit/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        

        FLAG_DIEHARDER = 1
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/dieharder/', shell = True)        
        out = subprocess.run(f'Tests/dieharder -d {param[config.ID]} -n {param[config.N_TUPL]} -f {test_file} -g 201', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')



        while(output_list[-1] == '' ):
            del output_list[-1]




        for line in output_list[8:]:
            if('PASSED' not in line):
                FLAG_DIEHARDER = 0
        
        
        if(FLAG_DIEHARDER == 0):
            print(f'\n!!! ALERT dieharder, {param[config.ID]}, {param[config.NAME]}, Tuple: {param[config.N_TUPL]}, iteration_{iteration}, core {core_no}, Failed !!!')
        else:
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]}, Tuple: {param[config.N_TUPL]}, iteration_{iteration}, core {core_no}, Passed')
    
        
        
        
        with open(f'{RESULT_DEST}/iteration_{iteration}/dieharder/{param[config.ID]}_{param[config.N_TUPL]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='dieharder'):
        
        
        FLAG_DIEHARDER = 1  
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/dieharder/', shell = True)  
        out = subprocess.run(f'Tests/dieharder -d {param[config.ID]} -f {test_file} -g 201', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split('\n')



        while(output_list[-1] == '' ):
            del output_list[-1]


        
        for line in output_list[8:]:
            if('PASSED' not in line):
                FLAG_DIEHARDER = 0
        

        
        if(FLAG_DIEHARDER == 0):
            print(f'\n!!! ALERT dieharder, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')
        else:
            print(f'\ndieharder, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
    
        


        with open(f'{RESULT_DEST}/iteration_{iteration}/dieharder/{param[config.ID]}.txt','w') as fw:
            for line in output_list:
                fw.write(line+'\n')
        
    
    
    
    
    
    
    
    
    
    
    elif(param[config.SUITE]=='nist'):
        
        
        FLAG_NIST = 1
        
        subprocess.run(f'mkdir -p {RESULT_DEST}/iteration_{iteration}/nist/{param[config.ID]}/{param[config.NAME]}/', shell = True)
        
        out = subprocess.run(f'Tests/nist {param[config.ID]} {test_file} {RESULT_DEST}/iteration_{iteration}/nist/{param[config.ID]} {param[config.SIZE]}', stdout=subprocess.PIPE, shell = True)
        output_list = (out.stdout.decode('utf-8')).split(' ')
        
        
        
        while("" in output_list):
            output_list.remove("") 
        
        
        
        for element in output_list[:-1]:
            if(int(element) < int(output_list[-1])):
                FLAG_NIST = 0
        
        
        if(FLAG_NIST == 0):
            print(f'\n!!! ALERT nist, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Failed !!!')
        else:
            print(f'\nnist, {param[config.ID]}, {param[config.NAME]}, iteration_{iteration}, core {core_no}, Passed')
    
    

    
    
    
    
    
    
    
    else:
        print('!!!INVALID TEST NOTICED!!!')
        return
    
    
    
    
    
    
    
    
    
    
    os.system(f'rm {test_file}')    #remove the random file created for the test.    
    process_time = time.time() - process_start_time    #time to execute the test.
    
    #storing details
    if(param[config.SUITE]=='dieharder' and 
         (param[config.ID] == '200' 
          or param[config.ID] == '201' 
          or param[config.ID] == '202' 
          or param[config.ID] == '203')):
        
        with open(f'{RESULT_DEST}/iteration_{iteration}/{param[config.SUITE]}_{param[config.ID]}_{param[config.N_TUPL]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    else:
        
        with open(f'{RESULT_DEST}/iteration_{iteration}/{param[config.SUITE]}_{param[config.ID]}_time.txt','w') as fw:
            fw.write(str(process_time))
    
    
    
    
    
    local_e.set()
    global_e.set()    #setting events