import os


def generator_method(output_file, file_size):
    '''
    

    Parameters
    ----------
    output_file : name/location of the file to be generated
    file_size : size of the file
    
    User defined function to creates the file

    Returns
    -------
    None.

    '''
    
    
    '''
    source_file = 'dieharder203.bin'        #source location
    
    
    if not hasattr(generator_method, "file_seek"):
        generator_method.file_seek = 0   #pointer in random file initialized.
                    
    if not hasattr(generator_method, "SOURCE_FILE_SIZE"):
        with open(source_file,'r') as fr:   #calculate file size for the first time.
            fr.seek(0,2)
            generator_method.SOURCE_FILE_SIZE = fr.tell()    
    
    #bin file creation for the test
    with open(source_file,'rb') as rf, open(output_file,'wb') as wf:
        
        #checking if file can be generated from current location else locate pointer at start of file.
        if(generator_method.file_seek + file_size > generator_method.SOURCE_FILE_SIZE):
            generator_method.file_seek = 0
        
        #reach to the required location.
        rf.seek(generator_method.file_seek, 0)
        
        #copying data to destination file
        wf.write(rf.read(file_size))
        #update pointer
        generator_method.file_seek = generator_method.file_seek + file_size
    '''
    os.system(f'EasyQuantis -p 0 -b {output_file} -n {file_size}')