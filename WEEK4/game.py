import random
def main():
    level = int(input("Level: "))
    cn = random.randint(1,level)
    guess = 0
    while True:
        guess=input("Guess: ")
        while guess.isnumeric()==False or int(guess)<1:
            guess=input("Guess: ")
        guess = int(guess)
        if guess<cn:
            print("Too small!")
        elif guess>cn:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
