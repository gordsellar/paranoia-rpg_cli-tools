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

# Pick a letter
def rando_letter(size=1, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

# Pick 3 alpha-numeric characters
def rando_sector(size=3, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Combine and print the name
print random.choice(get_name).strip() + "-" + rando_letter() + "-" + rando_sector()

fopen.close()
