def main():
    var=input('Enter the time please: ')
    var=convert(var)

    if 7<=var<=8:
        print("breakfast time")
    elif 12<=var<=13:
        print("lunch time")
    elif 18<=var<=19:
        print("dinner time")
    else:
        print("")


def convert(time):
    if len(time)==5:
        hr = float(time[0:2])
        mins = float(time[3:])/60
    else:
        hr = float(time[0:1])
        mins = float(time[2:])/60
    converted = hr+mins
    return converted



if __name__ == "__main__":
    main()
