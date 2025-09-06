def main():
    text = input("Enter your camelCase text: ")
    Text = list(text)
    for s in range(len(Text)):
        if Text[s] == Text[s].upper():
            Text[s] = f'_{Text[s].lower()}'

    print(''.join(Text))

main()
