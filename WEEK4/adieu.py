import inflect
import sys

def main():
    NAMEs=[]
    c = inflect.engine()

    while True:
        try:
            print('Name: ', end='')
            name=input()
            if len(NAMEs)==0 and name=='':
                sys.exit(0)
            NAMEs.append(name)
        except EOFError:
            break

    print(f"\nAdieu, adieu, to {c.join(NAMEs)}")

if __name__ == '__main__':
    main()
