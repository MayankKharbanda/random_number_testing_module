import config
from sys import exit


def test_reader(file):
    
    '''
    

    Parameters
    ----------
    file : path of configuration file from which data is to be taken.
    
    
    '#' is used to add comment in file.

    Returns
    -------
    tests : a list of all the tests to be run on the random numbers.

    '''

    
    tests=[]        # will contain list of all the tests to run.
    
    
    try:        
        with open(f'{file}','r') as f:
            file_data = f.readlines()
            
            
            
            
            for line_number in range(len(file_data)):   
            
                FLAG=0
                if(file_data[line_number].startswith('#')): #ignoring commented lines
                                   continue
            
                
                
                line_data = file_data[line_number].split(',')   #split data acc to ','
                for i in range(len(line_data)):
                    line_data[i] = line_data[i].strip()
                
                    if(line_data[i].startswith('#')):   #handling inline comments
                       FLAG=1
                       break

                
                
                
                
                if(FLAG == 0):      #handling inline comments
                    if(line_data[0:i+1] == [] or line_data[:] == ['']):
                        continue
                    tests.append(line_data[0:i+1])
                else:
                    if(line_data[0:i] == [] or line_data[:] == ['']):
                        continue
                    tests.append(line_data[0:i])
                
                
                
                
                #deleting the last blank elements, if any
                while(tests[-1][-1] == ''):
                    del tests[-1][-1]
                
                
                
                
                #checking for enough arguments
                if(len(tests[-1]) != 6 and len(tests[-1]) != 5):
                    print(f'!!! Error in line {line_number+1} in tests file, Number of arguments does not match. !!!')    
                    exit(0)
                    
                
                
                
                
                #handling special tests having different number of arguments
                if(tests[-1][config.SUITE]=='dieharder' and 
                   (tests[-1][config.ID] == '200' 
                    or tests[-1][config.ID] == '201' 
                    or tests[-1][config.ID] == '202' 
                    or tests[-1][config.ID] == '203')):
                    if(len(tests[-1]) != 6):
                        print(f'!!! Error in line {line_number+1} in tests file, Number of arguments does not match. !!!')
                        exit(0)
                
                elif(len(tests[-1]) != 5):
                    print(f'!!! Error in line {line_number+1} in tests file, Number of arguments does not match. !!!')
                    exit(0)
                
                
                
                
                try:    
                    #calculate size of the file required, if it is an expression.
                    tests[-1][config.SIZE] = str(eval(tests[-1][config.SIZE]))
                except:
                    print(f'!!! Error in file size in line number {line_number+1}, file size could not be evaluated. !!!')
                    exit()
    
    
    except FileNotFoundError:       #handling exception, if test file is not found.
        print(f'!!! ERROR: Test file at --{file}-- is not available. !!!')
        exit()                                                     
    
    
    
    
    
    if(len(tests) == 0):
        print(f'!!! ERROR: No tests in Test File. !!!')
        exit()                                                    

    return tests