import config
from sys import exit

'''
test_reader function is used to initialize the tests list from config file, 
passed as parameter.
'''


def test_reader(file):
    
    '''
    input: path of configuration file from which data is to be taken.
    output: returns a list of all the tests to be run on the random numbers.
    NOTE: The code is # sensitive, if there is # at any position in a line,
        the function would not read the line after that hash
    '''
    
    tests=[]        #contains list of all the tests to be checked.
    
    with open(file,'r') as f:
        
        file_data = f.readlines()
        
        for line_number in range(len(file_data)):
            
            flag=0
            
            if(file_data[line_number].startswith('#')):
                               continue
            
            line_data = file_data[line_number].split(',')
            
            for i in range(len(line_data)):
                line_data[i] = line_data[i].strip()
                
                if(line_data[i].startswith('#')):
                   flag=1
                   break
            
            if(flag == 0):
                tests.append(line_data[0:i+1])
            else:
                tests.append(line_data[0:i])
            
            if(len(tests[-1]) != 6 and len(tests[-1]) != 5):
                print(f'!!!Error in line {line_number} in tests file, unknown test type!!!')
                exit(0)
            
            if(tests[-1][config.SUITE]=='dieharder' and 
               (tests[-1][config.ID] == '200' 
                or tests[-1][config.ID] == '201' 
                or tests[-1][config.ID] == '202' 
                or tests[-1][config.ID] == '203')):
                if(len(tests[-1]) != 6):
                    print(f'!!!Error in line {line_number} in tests file, parameters incomplete or unknown test!!!')
                    exit(0)
                
            elif(len(tests[-1]) != 5):
                print(f'!!!Error in line {line_number} in tests file, parameters incomplete or unknown test!!!')
                exit(0)
            
            tests[-1][config.SIZE] = str(eval(tests[-1][config.SIZE]))      #calculate size of the 
                                                        #file required, if it is 
                                                        #an expression.

    return tests
