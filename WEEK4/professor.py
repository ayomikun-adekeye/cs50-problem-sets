import random

def main():
    score = 0
    n = get_level()
    Q = generate_integer(n)
    for x in range (10):
        print(f"{Q[0]} + {Q[1]} = ", end ="")
        ans = int(input())
#correcting my mistake
        if ans == Q[0]+Q[1]:
            score+=1
            Q.pop(0)
            Q.pop(0)
            continue
        else:
            print(f"EEE\n{Q[x]} + {Q[x+1]} = ", end ="")
            ans = int(input())
            if ans == Q[0]+Q[1]:
                score+=1
                Q.pop(0)
                Q.pop(0)
                continue
            else:
                print(f"EEE\n{Q[x]} + {Q[x+1]} = ", end ="")
                ans = int(input())
                if ans == Q[0]+Q[1]:
                    score+=1
                    Q.pop(0)
                    Q.pop(0)
                    continue
                else:
                    print(f"{Q[x]} + {Q[x+1]} = {Q[x]+Q[x+1]}")
    print(f"Score: {score}")

def get_level():
    level = input("Level: ")
    while (level != '1' and level != '2' and level != '3') or level.isnumeric()==False:
        level = input("Level: ")
    return int(level)

def generate_integer(lvl):
    '''
    I establish the boundaries for the randomly generated numbers depending on lvl, then I populate the initialised NUM list
    '''
    NUMs = []
    if lvl == 1:
        a,b = 0,9
    elif lvl == 2:
        a,b = 10,99
    else:
        a,b = 100,999
    for z in range(20):
        NUMs.append(random.randint(a,b))
    return NUMs

if __name__ == "__main__":
    main()
