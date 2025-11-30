# Abram Denzlinger
# November 28, 2025
# Module 9.2 - APIs

# This program uses an API to get and
# print information. It tests the connection, then
# prints the response code, then prints the
# unformatted data, and finally prints the formatted
# data via a function.

import requests
import json

def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://anapioficeandfire.com/api/houses")

# Printing the response code
print()
print("=" * 20)
print("Status Code: ")
print(response.status_code)
print("=" * 20)

# Printing the unformatted data
print()
print("=" * 20)
print("Unformatted Data: ")
print("=" * 20)
print(response.json())
print("=" * 20)

# Printing the formatted data
print()
print("=" * 20)
print("Formatted Data: ")
print("=" * 20)
formatted_print(response.json())


