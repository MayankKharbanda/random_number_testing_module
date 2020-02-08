import multiprocessing
import os


def process1(param, e):
    os.system(f'byte_stream/fast.sh {param}')
    e.set()

    
def process2(param, e):
    os.system(f'byte_stream/normal.sh {param}')
    e.set()



def process_initializer_1(e):
    for i in range(2,3):
        e.wait()
        p1 = multiprocessing.Process(target=process1, args=(i, e))    
        p1.start()
        e.clear()



def process_initializer_2(e):
    for i in range(2,3):
        e.wait()
        p2 = multiprocessing.Process(target=process2, args=(i, e))
        p2.start()
        e.clear()



process_complete_events = []
process_initializers = []



for i in range(2):
    process_event = multiprocessing.Event()
    process_event.set()
    process_complete_events.append(process_event)

process_initializer1 = multiprocessing.Process(target=process_initializer_1, args=(process_complete_events[0],))
process_initializers.append(process_initializer1)
process_initializer1.start()

process_initializer2 = multiprocessing.Process(target=process_initializer_2, args=(process_complete_events[1],))
process_initializers.append(process_initializer2)
process_initializer2.start()
        
    
for p in process_initializers:
    p.join()