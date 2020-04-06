#Cleaning and Preparing Data in Python: Takeaways
#by Dataquest Labs, Inc. - All rights reserved © 2020
#Syntax
#TRANSFORMING AND CLEANING STRINGS
#Replace a substring within a string:

green_ball = "red ball".replace("red", "green")

#Remove a substring:

friend_removed = "hello there friend!".replace(" friend", "")

#Remove a series of characters from a string:

bad_chars = ["'", ",", ".", "!"]
string = "We'll remove apostrophes, commas, periods, and exclamation marks!"
for char in bad_chars:
    string = string.replace(char, "")

#Convert a string to title cases:

Hello = "hello".title()

#Check a string for the existence of a substring:

if "car" in "carpet":
    print("The substring was found.")
else:
    print("The substring was not found.")

#Split a string into a list of strings:

split_on_dash = "1980-12-08".split("-")

#Slice characters from a string by position:

last_five_chars = "This is a long string."[:5]

#Concatenate strings:

superman = "Clark" + " " + "Kent"

#Concepts
#When working with comma separated value (CSV) data in Python, it's common to have your data in a "list of lists" format, where each item of the internal lists are strings.
#If you have numeric data stored as strings, sometimes you will need to remove and replace certain characters before you can convert the strings to numeric types, like int and float.
#Strings in Python are made from the same underlying data type as lists, which means you can index and slice specific characters from strings like you can lists.
#Resources
#Python Documentation: String Methods
