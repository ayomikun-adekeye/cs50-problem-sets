import sys

def main():
    if len(sys.argv)==1:
        sys.exit('Too few command-line arguments')
    if len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    if sys.argv[1][-3:]!='.py':
        sys.exit('Not a Python file')

    print(LOC(sys.argv[1]))


def LOC(file_name):
    loc = 0
    with open(file_name) as file:
        for line in file:
            if line.strip() == '':
                continue
            elif line.lstrip().startswith('#'):
                continue
            else:
                loc+=1
    return loc

main()


