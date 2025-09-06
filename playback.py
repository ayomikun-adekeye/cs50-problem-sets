def slow_down(text):
    text = text.replace(" ","...")
    return text

test = input("Enter some test text please: ")
print(slow_down(test))
