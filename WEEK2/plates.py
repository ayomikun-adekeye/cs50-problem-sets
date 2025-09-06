NUM = ['0','1','2','3','4','5','6','7','8','9']
ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def two_letters(s):
    if length(s) == False:
        return False
    if s[0] in NUM:
        return False
    if s[1] in NUM:
        return False
    else:
        return True #CRI 1 DOWN

def length(s):
    if (2<=(len(s))<=6):
        return True
    else:
        return False # CRI 2 DOWN

def num_position(s):
    i = 0
    if s.isalpha() == True:
        return True
    else:
        while i!=len(s):
            if s[i] in NUM:
                if s[i] == s[-1]:
                    return True
                elif s[i:].isnumeric() == False:
                    return False
                else:
                    return True
            i+=1

def zero(s):
    i = 0
    while i != len(s):
        if s.isalpha() == True:
            return True
        if s[i] in NUM:
            if s[i] == '0':
                return False
            else:
                return True
        i += 1

def punc(s):
    for x in s:
        if x not in ALPHA:
            if x not in NUM:
                return False
        if x not in NUM:
            if x not in ALPHA:
                return False
        return True


def is_valid(s):
    if two_letters(s) and length(s) and num_position(s) and zero(s) and punc(s):
        return True
    else:
        return False

main()
