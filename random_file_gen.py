import config
import os

def inorder_file_gen(Tests, inorder_file_event):
    
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