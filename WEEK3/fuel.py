def main():
    level =  valid()
    level = round(level)
    if level <= 1:
        print('E')
    elif level >= 99:
        print('F')
    else:
        print(f'{level}%')



def valid():
    while True:
        try:
            n = slash()
            X = int(val[0:n])
            Y = int(val[(n+1):])
            if (X/Y)*100>100 or (X/Y)*100<0:
                n = slash()
            return (X/Y)*100
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

def slash():
    global val
    val = input("Fraction: ")
    while '/' not in val:
        val = input("Fraction: ")
    for s in val:
        if s == '/':
            return val.index(s)

main()
