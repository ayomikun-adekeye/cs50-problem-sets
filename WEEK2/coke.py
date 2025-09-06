def main():
    pay = 0
    amount_due = 50
    print (f"Amount due: {amount_due}")
    while pay < 50:
        coin = collect()
        pay = pay + coin
        amount_due = 50 - pay
        print(f"Amount Due: {amount_due}")
    owe = (-1*amount_due)
    print(f"Change Owed: {owe}")

def collect():
    while True:
        n = int(input("Insert coin: "))
        if n != 5 and n != 10 and n != 25:
            print("Amount Due: 50")
            continue
        else:
            return n

main()
