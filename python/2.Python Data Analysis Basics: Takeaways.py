#Python Data Analysis Basics: Takeaways
#by Dataquest Labs, Inc. - All rights reserved © 2020
#Syntax
#STRING FORMATTING AND FORMAT SPECIFICATIONS
#Insert values into a string in order:

continents = "France is in {} and China is in {}".format("Europe", "Asia")

#Insert values into a string by position:

squares = "{0} times {0} equals {1}".format(3,9)

#Insert values into a string by name:

population = "{name}'s population is {pop} million".format(name="Brazil", pop=209)

#Format specification for precision of two decimal places:

two_decimal_places = "I own {:.2f}% of the company".format(32.5548651132)

#Format specification for comma separator:

india_pop = The approximate population of {} is {}".format("India",1324000000)

#Order for format specification when using precision and comma separator:

balance_string = "Your bank balance is {:,.2f}"].format(12345.678)

#Concepts
#The str.format() method allows you to insert values into strings without explicitly converting them.
#The str.format() method also accepts optional format specifications, which you can use to format values so they are easier to read.
#Resources
#Python Documentation: Format Specifications
#PyFormat: Python String Formatting Reference
