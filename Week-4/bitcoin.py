import sys
import requests


def main():
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = r.json()["bpi"]["USD"]["rate_float"]
    try:
        quantidade = float(sys.argv[1])
        quantidade = quantidade * bitcoin
        print(f"${quantidade:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    except IndexError:
        print("Missing command-line argument")
        sys.exit(1)


main()
