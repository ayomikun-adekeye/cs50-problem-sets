Vowels = ["a","e","i","o","u","A","E","I","O","U"]

def main():
    docs = input("Input: ")
    print(shorten(docs))
    return shorten(docs)

def shorten(word):
    word = list(word)
    for i in range(len(word)):
        if word[i] in Vowels:
            word[i] = ""
    return ''.join(word)

if __name__ == "__main__":
    main()
