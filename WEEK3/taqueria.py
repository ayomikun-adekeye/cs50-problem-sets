MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    try:
        while True:
            order = input("Item: ").title()
            while MENU.get(order) == None:
                order = input("Item: ").title()
            total = total + MENU[order]
            print(f"Total: ${total:.2f}")
    except EOFError:
        print(" ")

main()
