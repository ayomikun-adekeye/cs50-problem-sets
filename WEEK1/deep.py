value = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
value = value.strip().lower()

if 'forty' in value:
    if 'two' in value:
        print('Yes')
    else:
        print('No')
elif '42' == value:
    print('Yes')
else:
    print('No')
