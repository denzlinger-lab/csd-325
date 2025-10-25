# Abram Denzlinger
# Assignment 1.3 - 99 Bottles
# October 23, 2025

# prompts user for # of bottles
# uses a while loop to iterate down to 1
# and prints verses
# prints unique verses for 1 bottle and 0 bottles

bottles_beer = int(input("How many bottles of beer do you have?"))

while bottles_beer > 2:
    print(f"{bottles_beer} bottles of beer on the wall")
    print(f"{bottles_beer} bottles of beer")
    bottles_beer -= 1
    print(f"take 1 down, pass it around,")
    print(f"{bottles_beer} bottles of beer on the wall")
    print()

print(f"{bottles_beer} bottles of beer on the wall")
print(f"{bottles_beer} bottles of beer")
bottles_beer -= 1
print(f"take 1 down, pass it around,")
print(f"{bottles_beer} bottle of beer on the wall")
print()

print(f"{bottles_beer} bottle of beer on the wall")
print(f"{bottles_beer} bottle of beer")
bottles_beer -= 1
print(f"take 1 down, pass it around,")
print(f"{bottles_beer} bottles of beer on the wall")
print()