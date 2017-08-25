#Variables
#Creating web apps, games, and search engines all involve storing and working with different types of data. They do so using variables. A variable stores a piece of data, and gives it a specific name.
#For example:
#spam = 5
#The variable spam now stores the number 5.

# Write your code below!
my_variable = 10

#Booleans
#Great! You just stored a number in a variable. Numbers are one data type we use in programming. A second data type is called a boolean.
#A boolean is like a light switch. It can only have two values. Just like a light switch can only be on or off, a boolean can only be True or False.
#You can use variables to store booleans like this:

a = True
b = False

# Set the variables to the values listed in the instructions!

my_int = 7
my_float = 1.23
my_bool = True

#You've Been Reassigned
#Now you know how to use variables to store values.
#Say my_int = 7. You can change the value of a variable by "reassigning" it, like this:

my_int = 3

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

my_int = 10

print my_int

#Whitespace
#In Python, whitespace is used to structure code. Whitespace is important, so you have to be careful with how you use it.
#In Python you can either indentate by using "spaces" or by using the "tab" key but not BOTH

#bad indented code:
def spam():
eggs = 12;
return eggs

print spam()

#correct indentation:
def spam():
  eggs = 12
  return eggs

print spam()

#Single Line Comments
#You probably saw us use the # sign a few times in earlier exercises. The # sign is for comments. A comment is a line of text that Python won't try to run as code. It's just for humans to read.
#Comments make your program easier to understand. When you look back at your code or others want to collaborate with you, they can read your comments and easily figure out what your code does.
#Example of a comment.

mysterious_variable = 42

#Multi-Line Comments
#The # sign will only comment out a single line. While you could write a multi-line comment, starting each line with #, that can be a pain.
#Instead, for multi-line comments, you can include the whole block in a set of triple quotation marks:

"""Sipping from your cup 'til it
runneth over,
Holy Grail."""

#Math
#Great! Now let's do some math. You can add, subtract, multiply, divide numbers like this
#addition = 72 + 23
#subtraction = 108 - 204
#multiplication = 108 * 0.5
#division = 108 / 9

# Set count_to equal to the sum of two big numbers

count_to = 194245 + 519593

print count_to

#Exponentiation
#All that math can be done on a calculator, so why use Python? Because you can combine math with other data types (e.g. booleans) and commands to create useful programs. Calculators just stick to numbers.
#Now let's work with exponents.
#eight = 2 ** 3
#In the above example, we create a new variable called eight and set it to 8, or the result of 2 to the power to 3 (2^3).
#Notice that we use ** instead of * or the multiplication operator.

#Set eggs equal to 100 using exponentiation on line 3!

eggs = 10**2

print eggs

#Modulo
#Our final operator is modulo. Modulo returns the remainder from a division. So, if you type 3 % 2, it will return 1, because 2 goes into 3 evenly once, with 1 left over.

#Set spam equal to 1 using modulo on line 3!
spam = 20 % 19

print spam

#Bringing It All Together
#Nice work! So far, you've learned about:
#Variables, which store values for later use
#Data types, such as numbers and booleans
#Whitespace, which separates statements
#Comments, which make your code easier to read
#Arithmetic operations, including +, -, *, /, **, and %
# Below are some very important variables.

monty = True
python = 1.234
monty_python = python ** 2

#Project 1
#TIP CALCULATOR
#    The Meal
#   Now let's apply the concepts from the previous section to a real world example.

#   You've finished eating at a restaurant, and received this bill:

#Cost of meal: $44.50
#Restaurant tax: 6.75%
#Tip: 15%
#You'll apply the tip to the overall cost of the meal (including tax)

# Reassign meal on line 7!
# Assign the variable total on line 8!

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax #Reassigning the value of the meal in a Single Line
total = meal + meal * tip #Reassigning the value of the meal in a Single Line

print("%.2f" % total) #Prints the total with exactly two decimals

#Strings

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line
print caesar
print praline
print viking

#Fixing strings on Python:

# The string below is broken. Fix it using the escape backslash!
#Some characters cause issues on Python the use of \ before the character fixes the issue
"""This isn\'t flying, this is falling with style!"""

#Access by Index

#Each character in a string is assigned a number. This number is called the index. Check out the diagram in the editor.

#c = "cats"[0]
#n = "Ryan"[3]
#In the above example, we create a new variable called c and set it to "c", the character at index zero of the string "cats".
#Next, we create a new variable called n and set it to "n", the character at index three of the string "Ryan".
#In Python, we start counting the index from zero instead of one.

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

#String methods let you perform specific tasks for strings.

#We'll focus on four string methods:

#len()
#lower()
#upper()
#str()
#Let's start with len(), which gets the length (the number of characters) of a string!

#len() method
parrot = "Norwegian Blue"
print len(parrot)

#lower() method
parrot = "Norwegian Blue"
print parrot.lower()

#upper() method
parrot = "norwegian blue"
print parrot.upper()

#str() converts non-strings into strings
pi = 3.14
print str(pi)

#Dot Notation
#Let's take a closer look at why you use len(string) and str(object), but dot notation (such as "String".upper()) for the res

lion = "roar"
len(lion)
lion.upper()

######################################################
#Methods that use dot notation only work with strings.
#On the other hand, len() and str() can work on other data types

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#Printing Strings
#The area where we've been writing our code is called the editor.
#The console (the window to the right of the editor) is where the results of your code is shown.
#print simply displays your code in the console.

#Turn 3.14 into a string by using str() method
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

#String Formatting with %, Part 1
#When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)
#The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.

#String formatting with % can be really useful
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
#prints Let's not go to Camelot. 'Tis a silly place.

#String Formatting example
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
#prints:
#What is your name? Rob
#What is your quest? To learn programming
#What is your favorite color? Green
#Ah, so your name is Rob, your quest is To learn programming, and your favorite color is Green.

######################## Summary ##########################
#And Now, For Something Completely Familiar

#Three ways to create strings
'Alpha'
"Bravo"
str(3)

#String methods
len("Charlie")
"Delta".upper()
"Echo".lower()

#Printing a string
print "Foxtrot"

#Advanced printing techniques
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)
