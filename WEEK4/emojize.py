import emoji

def main():
    print("Input: ", end="")
    print(emoji.emojize(input(), language='alias'))
main()
