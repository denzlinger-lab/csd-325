import random
from os import WCONTINUED

# Scratchpad
# Testing various solutions

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

roll_total = dice1 + dice2

print('    ', dice1, '-', dice2)
print('    ', roll_total)

if roll_total == 2 or roll_total == 7:
    print(f'You rolled a {roll_total}, you get a 10 mon bonus!')
else:
    print('No bonus for this roll.')

