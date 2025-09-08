import requests
import sys # to work with command-line arguements
import json # to work with JSON objects

try:
    #how much bitcoin to buy
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line arguement")
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    #querying the API for the price of one, and displaying the total price
    data = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=ab78d2f99ef345dc65b146791a2f6d4b192dca84359e7273aaefb6b62dff3213').json()
    price = float(data["data"]["priceUsd"])
    print(f"${(n*price):,.4f}")
except requests.RequestException:
    pass
