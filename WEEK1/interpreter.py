express = input("Expression please: ")
if len(express)== 5:
    x = int(express[0])
    y = express[2]
    z = int(express[-1])
else:
    if express[1] != '+' and express[1] != '-' and express[1] != '*' and express[1] != '/':
        x = int(express[0:2])
        y = express[-3]
        z = int(express[-1])

match y:
    case '+':
        ans = x+z
        print(float(ans))
    case '-':
        ans = x-z
        print(float(ans))
    case '*':
        ans = x*z
        print(float(ans))
    case '/':
        if z != 0:
            ans = x/z
            print(float(ans))
        else:
            print("Zero Error!")
    case _:
        print("Operator Error!")
