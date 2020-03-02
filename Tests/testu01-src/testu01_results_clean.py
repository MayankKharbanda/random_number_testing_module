tests=[]
pass_count=0
count=0
with open('results_crush.txt','r') as f:
    read_file = iter(f)
    for line in read_file:
        if 'Generator providing data from binary file.' in line and 'Generator:        Generator providing data from binary file.' not in line:
            line=next(read_file)
            line=next(read_file)
            line=next(read_file)
            if line not in tests:
                tests.append(line)
        if 'All tests were passed' in line:
            pass_count=pass_count+1
        if 'Summary results of Crush' in line:
            count=count+1
print(count)
print(len(tests))
print(pass_count)