Vowels = ["a","e","i","o","u","A","E","I","O","U"]

def main():
    text = input("Input: ")
    text = list(text)
    for i in range(len(text)):
        if text[i] in Vowels:
            text[i] = ""
    print(''.join(text))

main()
