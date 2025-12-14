#abram denzlinger
#August 26, 2025
#Module 4.2 Assignment (main)
#This is a program to convert miles to km
#Uses try/except blocks for user input validation

#function converts miles to kilometers
def miles_to_km(miles):
    kilometers = miles * 1.60934
    return kilometers

#user input, converting to float, assigning to variable, validation
while True:
    try:
        text = input('Enter the # of miles driven: ')
        try:
            miles = float(text)
            if miles < 0:
                print('Error - miles must be greater than 0. Try again.')
                continue
            break
        except ValueError:
            print('Error - please enter a numeric value.')
        miles = float(input('Enter the # of miles driven: '))
        break
    except ValueError:
        print('Error - please enter a numeric value.')

#final output, calling the function, formatting
print(f'Your {miles} mile trip is equal to {miles_to_km(miles):.2f} kilometers.')
