def config(file):
    tests=[]
    with open(file,'r') as f:
        for line in f.readlines():
            if('#' in line):
               continue
            tests.append(line.split(','))
           
    for test in range(len(tests)):
        for data in range(len(tests[test])):
            tests[test][data] = tests[test][data].strip()
    return tests