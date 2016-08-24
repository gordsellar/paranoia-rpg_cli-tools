#!/usr/bin/python
#
# This is a VERY simple Python script to generate character names for Paranoia.
# All names follow the convention of Firstname-SingleLetter-AlphaNumeric(times 3)
# 	Example: ALAN-R-7R2
#
# The list of names was taken from a US Census list of Male and Female first names
#
# 	Source URL: http://deron.meranda.us/data/census-derived-all-first.txt
#
# There are probably ways to simplify the code, but for now it works
#
# Don't forget... Fun is Mandatory!
# 	- BanjoFox!
#

import string
import random

# Open the name file as read-only
fopen = open("names.txt", "r")
get_name = file.readlines(fopen) 

# Randomize and pick some letters then return them in the N-NNN format
def rando_suffix(size=0, chars=string.ascii_uppercase):
	suffix1 = ''.join(random.choice(chars) for _ in range(1))
	suffix3 = ''.join(random.choice(chars) for _ in range(3))
	suffix = suffix1 + "-" + suffix3
	return suffix

# Finally, pick a number
def rando_num(size=1, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


# Prompt for user input
usr_in = input("How many names would you like? ")

# Create a number of names until the value equals the user selected value
count = 0 
while count < usr_in:

	# Combine and print the name
	print random.choice(get_name).strip() + "-" + rando_suffix() + "-" + rando_num()
	count +=1

# Cleanup 
fopen.close()
