GROCERIES = {}
groc_list =[]
def main():
    try:
        while True:
            item = input()
            groc_list.append(item.upper())
    except EOFError:
        global GROCERIES
        sort(groc_list)
        KEYS = list(GROCERIES.keys())
        VALUES = list(GROCERIES.values())
        for d in range(len(KEYS)):
            print(f"{VALUES[d]} {KEYS[d]}")


def sort(LIST):
    global GROCERIES
    for n in range(len(LIST)):
        if LIST[n] in GROCERIES == True:
            continue
        GROCERIES[LIST[n]] = LIST.count(LIST[n])
    GROCERIES = dict(sorted(GROCERIES.items()))




main()
