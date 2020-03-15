
'''
This is user defined function to generate random numbers.
Change according to your random number generator.
'''

def generator_method(output_file, file_size):
    
    '''
    input-
    output_file: the location/name of the output file to be generated.
    file_size: the size of file(in bytes) to be created.
    
    Edit code below according to your generator.
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