import re
i=1
'''
with open('Tests/testu01-src/crush_desc.md','r') as fr, open('config.txt','a+') as fw:
    for line in fr.readlines():
        x = line.split(sep='|')
        if(len(x)>1 and re.search(r'[0-9]',x[1])):
            fw.write(f'{i},\tcrush,\t\t{x[2].strip()},\t\t{i},\tNone,\n')
            i=i+1
'''
'''
with open('Tests/testu01-src/big_crush_desc.md','r') as fr, open('config.txt','a+') as fw:
    for line in fr.readlines():
        x = line.split(sep='|')
        if(len(x)>1 and re.search(r'[0-9]',x[1])):
            fw.write(f'{i},\tbigcrush,\t{x[2].strip()},\t\t{i},\tNone,\n')
            i=i+1
'''
'''
with open('Tests/NIST-Test-Suite/README.md','r') as fr, open('config.txt','a+') as fw:
    for line in fr.readlines():
        x = line.split(sep='-')
        if(x[0]==''):
            fw.write(f'{i},\tnist,\t\t{x[1].strip()},\t\t{i},\tNone,\n')
            i=i+1
'''
with open('Tests/dieharder_install/README.md','r') as fr, open('config.txt','a+') as fw:
    for line in fr.readlines():
        x = line.split()
        if(len(x)>1 and re.search(r'[0-9]',x[0])):
            s=' '
            fw.write(f'{i},\tdieharder,\t{s.join(x[2:])},\t\t\t\t{x[1]},\tNone,\n')

            i=i+1