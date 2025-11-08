# Abram Denzlinger
# November 8, 2025
# Assignment 4.2 - Sitka Weather

# This program reads temperatures and dates from a csv
# file and plots them on a line graph. It takes user input
# to determine whether it reads and plots high temperatures
# or low temperatures, and also gives the user an option to
# exit the program.

# My initial approach was to initialize lists for both highs
# and lows, and then only plot according to user input. Dialogue
# with Gemini explained while technically correct, that wasn't the
# most efficient approach. This version only extracts and plots the
# needed data, and is therefore more efficient.

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 1. Configuration Map
# Maps user input to (column_index, plot_title_label, plot_color)
COLUMN_MAP = {
    'highs': (5, "Daily High Temperatures", 'red'),
    'lows': (6, "Daily Low Temperatures", 'blue')
}

# 2. Get User Input
while True:
    choice = input("View (Highs), or (Lows), or (Exit)? ").strip().lower()
    if choice in ['exit', 'quit']:
        print("Thank you, goodbye!")
        exit()

    if choice in COLUMN_MAP:
        break
    print("Invalid choice. Please type 'highs', 'lows', or 'exit'.")

# Get the necessary info based on the valid choice
DATA_COLUMN, PLOT_LABEL, PLOT_COLOR = COLUMN_MAP[choice]


# 3. Data Extraction and Processing
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Initialize lists to store the required data
    dates, temperatures = [], []

    # Process each row
    for row in reader:
        try:
            # Date is always in column 2
            current_date = datetime.strptime(row[2], '%Y-%m-%d')

            # Temperature column index is based on user's choice
            temp = int(row[DATA_COLUMN])
        except ValueError:
            # Skip rows with missing or invalid data
            print(f"Skipping row due to missing data: {row}")
            continue

        dates.append(current_date)
        temperatures.append(temp)


# 4. Plotting and Formatting
fig, ax = plt.subplots(figsize=(10, 6)) # Set a standard figure size
ax.plot(dates, temperatures, c=PLOT_COLOR, linewidth=2)

# Format plot.
plt.title(f"{PLOT_LABEL} - 2018", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate() # Rotate x-axis date labels
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()