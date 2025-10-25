# Abram Denzlinger
# Assignment 1.3 - 99 Bottles
# October 23, 2025

# program to sing 99 bottles of beer
# prompts user for # of bottles
# validates input for whole, non-zero number
# uses a for loop to iterate through range, printing verses
# defines "bottles_text" variable to handle changing
# "bottles" to "bottle"
# uses if statement to format final verse

def sing_bottles_of_beer():
    # Prompt user for starting bottles. Validate for whole number and > 0.
    while True:
        try:
            start_bottles = int(input("How many bottles of beer should we start with? "))

            if start_bottles <= 0:
                print("Please enter a number greater than 0. ")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Start the loop from the user's chosen number
    for num_bottles in range(start_bottles, 0, -1):
        # Format the lyrics for the current number of bottles
        bottles_text = "bottles" if num_bottles > 1 else "bottle"

        # Print the verse for each iteration
        print(f"{num_bottles} {bottles_text} of beer on the wall,")
        print(f"{num_bottles} {bottles_text} of beer.")

        # Format the next line of lyrics
        next_num = num_bottles - 1
        if next_num == 0:
            next_line = "no more bottles of beer on the wall."
        else:
            next_bottles_text = "bottles" if next_num > 1 else "bottle"
            next_line = f"{next_num} {next_bottles_text} of beer on the wall."

        print(f"Take one down and pass it around, {next_line}\n")

    # Print the final verse
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, then you'll have more beer on the wall!")

# Run the function to start the song
sing_bottles_of_beer()
