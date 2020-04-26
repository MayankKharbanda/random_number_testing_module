class File_gen:
    
    #class used to crete objects for file_gen queue
    
    def __init__(self, 
                 start_time = None, 
                 core = None, 
                 test_number = None):
        '''
        

        Parameters
        ----------
        start_time : Start time of test.
        core : Core number on which test is allocated.
        test_number : Test number.

        '''

        self.start_time = start_time
        self.core = core
        self.test_number = test_number