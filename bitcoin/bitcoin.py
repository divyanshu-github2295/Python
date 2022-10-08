import sys
import requests


def main():

    # Getting number of bitcoins
    bitcoin = get_bitcoin()

    # Getting real-time price for bitcoin
    price = get_price()

    # Calculating total price
    amount = bitcoin * price

    print(f"${amount:,.4f}")


# Checking and converting command-line argument
def get_bitcoin():

    if len(sys.argv) == 2:
        try:
            bit = float(sys.argv[1])
            return bit
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


# Getting Bitcoin Price
def get_price():

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        index = response.json()
        return index["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
