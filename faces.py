def main():
    test = input()
    print(convert(test))

def convert(string):
    step_one = string.replace(":)","🙂")
    step_two = step_one.replace(":(","🙁")
    return step_two

main()
