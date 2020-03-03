import config

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
        
        for line in f.readlines():
            
            flag=0
            
            if(line.startswith('#')):
                               continue
            
            line_data = line.split(',')
            
            for i in range(len(line_data)):
                line_data[i] = line_data[i].strip()
                
                if(line_data[i].startswith('#')):
                   flag=1
                   break
            
            if(flag == 0):
                tests.append(line_data[0:i+1])
            else:
                tests.append(line_data[0:i])
            
            tests[-1][config.SIZE] = str(eval(tests[-1][config.SIZE]))      #calculate size of the 
                                                        #file required, if it is 
                                                        #an expression.

    return tests
