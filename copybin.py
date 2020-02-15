with open('dieharder_203.bin','rb') as rf, open('random_numbers_time/bigcrush54.bin','ab') as wf:
    #wf.seek(6, 0)
    #0 - offset is relative to start of file
    #1 - offset is relative to current position
    for _ in range(2):
        wf.write(rf.read(1_250_000_000))