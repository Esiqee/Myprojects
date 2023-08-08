import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    x = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = response.json()
#print(r)
price = r["bpi"]["USD"]["rate_float"]
#print(price)
output = float(price) * float(sys.argv[1])
print(f"${output:,.4f}")
