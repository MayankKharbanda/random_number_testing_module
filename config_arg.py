import argparse

def parse_arg():
    
    '''
    The function takes command line arguments.

    Returns
    -------
    args : all the argument values.

    '''
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--iteration", dest = "iteration", default = "-1", help="Number of iterations", type=int)
    #number of iterations/sample_size to run on test file. default:infinite.
    
    parser.add_argument("-t", "--tests_file", dest = "tests_file", help="Location of file containing tests to execute", type=str, required=True)
    #path to test file, containing description of all the tests to run(Compulsory).
    
    parser.add_argument("-d", "--dest_loc", dest = "dest_loc", default = "results", help="Location where the results are stored", type=str)
    #destination to store result.
    
    parser.add_argument("-c", "--cores", dest = "cores", default = "4", help="Number of cores for process, it allocates n-1 cores to tests and 1 core in file generation", type=int)
    #number of cores to make a process for each to run tests.
    
    parser.add_argument("-td", "--temp_dest", dest = "temp_dest", default = "temp_dest", help="temporary destination to store files", type=str)
    #temporary destination to store temporary data.
    
    parser.add_argument("-m", "--max_size", dest = "max_size", default = "10_000_000_000", help="Maximum file size generated", type=int)
    #maximum size of the file to be created for testing.
    
    args = parser.parse_args()
    
    return args