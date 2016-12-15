# # substitute value 10 with %d
# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
#
# # substitute the 2 %'s with strings above
# y = "Those who know %s and those who know %s." % (binary, do_not)
#
# print(x)
# print(y)
#
# # place string x inside string
# print("I said: %r." % x)
#
# hilarious = False
#
# # place string inside string
# joke_evaluation = "Isn't that joke so funny?! %r"
#
# print(joke_evaluation %hilarious)
#
# w = "This is the left side of..."
# e = "a string with a right side."
#
# print(w + e)

# print("Mary had a little lamb")
# print("It's fleece was white as %s." % 'snow')
# print("And everywhere that Mary went")
# print("." * 10)
#
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
#
# print(end1 + end2, end='')
# print(end3 + end4 + end5)

# formatter = "%r %r %r %r"
# print(formatter % (1,2,3,4))
# print(formatter % ("one", "two", "three", "four"))
# print(formatter % (True, False, False, True))
# print(formatter % (formatter, formatter, formatter, formatter))
# print(formatter % (
#     "I had this thing.",
#     "That you could type up right.",
#     "But it didn't sing.",
#     "So I said goodnight."
# ))

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print("Here are the days: ", days)
# print("Here are the months:\n", months)


# print("""
# There's \nsomething goin on here.
# With the three double-quotes.
# We'll be %s able to type as much as we like.
# """ % 'blah')


# tabby_cat = "\b I'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \v a \n cat."
#
# fat_cat = """
# I'll do a list:
# \t* Cat Food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
#
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print("%r\r" % i)

# print("How old are you?", end='')
# age = input()
# print("How tall are you?", end='')
# height = input()
# print("How much do you weigh?", end='')
# weight = input()
#
# print("So you're %r old, %r tall and %r heavy." % (age, height, weight))

# person = input('Enter your name:')
# print("Hello \t", person)

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")
# print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#   open file and return a stream\
# os
#   os.path, os.name, os.curdir, os.pardir

# pass variables to a script. Called argument
# from sys import argv
#
# script, first, second, third = argv
# fourth = input("What is your fourth variable? ")
#
# print("All together, your script is called %r, your first variable is %r, your second is %r, your third is %r, "
#       "and your fourth is %r" %(script, first, second, third, fourth))
#
## difference between input and argv. Argv - give your script inputs on command line, Input - input using keyboard
## while script is running

# from sys import argv
# script, user_name, friend = argv
# prompt = '=====> '
#
# print("Hi %s, I'm the %s script." %(user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do you like me %s?" % user_name)
# likes = input(prompt)
#
# print("where do you live %s?" %(user_name))
# lives = input(prompt)
#
# print("What kind of computer do you have?")
# computer = input(prompt)
#
# print("So %s, I want to talk to %s. What does he/she like?" %(user_name, friend))
# friend_like = input(prompt)
#
# print("""
# Alright so you have said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# It's cool that your friend has an interest in %r.
# """ % (likes, lives, computer, friend_like))

# # import argv from sys module
# from sys import argv
# # unpack parameters, give script parameters on command line
# script, filename = argv
# # open the text file
# txt = open(filename)
# # print string
# print("Here is your file %r:" % filename)
# # read contents of the file that was opened
# print(txt.read())
# # print string
# print("Type the filename again:")
# # user input while python executing
# file_again = input(">")
# # open file specified by user
# txt_again = open(file_again)
# # read opened file
# print(txt_again.read())

# # import argv from sys module
# from sys import argv
# # unpack parameters, give script parameters on command line
# script, username = argv
# # open the text file
#
# print("Hi %s! What file do you want to open?" % username)
# filename = input("What is your filename? >")
# with open(filename) as f:
#     for line in f:
#         print(line.split())

# import argv from sys module
# from sys import argv
# # unpack parameters, give script parameters on command line
# script, username = argv
# open the text file

# print("Hi %s! What file do you want to open?" % username)
# filename = input("What is your filename? >")
# txt = open(filename)
# print(txt.readlines())
# txt.close()

# close, read, readline, truncate, write

# grab argv module from sys package
# from sys import argv
#
# # unpack parameters to argv
# script, filename = argv
# # print("We're going to erase %r." % filename)
# # print("If you don't want that, hit CRTL-C (^C).")
# # print("If you do want that, hit RETURN.")
# #
# # input("?")
#
# print("Opening the file...")
# # open the file and grant write access
# target = open(filename, 'w')
#
# # print("Truncating the file. Goodbye!")
# # target.truncate()
#
# print("Now I'm going to ask you for three lines.")
#
# # user inputs for each each line to be written into file
# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")
#
# print("I'm going to write these to the file.")
#
# # writes use inputs into file
# # target.write(line1)
# # target.write("/n")
# # target.write(line2)
# # target.write("/n")
# # target.write(line3)
# # target.write("/n")
#
# target.write("%s /n %s /n %s /n" % (line1, line2, line3))
#
# print("And finally, we close it.")
# target.close()

# # truncate() not necessary with the 'w' parameter since when write to file will overwrite
# # modifiers - 'w+' 'r+' and 'a+' (will open file in both read and write mode)

# from sys import argv
# # checks if file exists
# from os.path import exists
# script, from_file, to_file = argv
#
# print("Copying from %s to %s" % (from_file, to_file))
#
# # we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
#
# print("The input file is %d bytes long" % len(indata))
#
# print("Does the ouput file exist? %r" % exists(to_file))
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print("Alright, all done")
# out_file.close()
# in_file.close()

# open("new.txt", 'w').write(open("blah.txt", 'r').read())

# def print_two(*args):
#     arg1, arg2 = args
#     print("arg1: %r, arg2: %r" % (arg1, arg2))
#
# def print_two_again(arg1, arg2):
#     print("arg1: %r, arg2: %r" % (arg1, arg2))
#
# def print_one(arg1):
#     print("arg1: %r" % (arg1))
#
# def print_none():
#     print("I got nothin'.")
#
# print_two("Zed", "Shaw")
# print_two_again("Zed", "Shaw")
# print_one("First!")
# print_none()

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print("You have %d cheeses!" % cheese_count)
#     print("You have %d boxes of crackers!" % boxes_of_crackers)
#     print("Man that's enough for a party!")
#     print("Get a blanket. \n")
#
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)
#
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# with open("new.txt", 'w') as Test1:
#     Test1.write("This is line 1\nThis is line 2\nThis is line 3\n")
#     Test1.close()

# # Unpack parameters to argv
# from sys import argv
#
# script, input_file = argv
#
# # create function that reads file
# def print_all(f):
#     print(f.read())
#
# # move pointer to beginning of file where starts reading
# # Each time you do f.seek(0), you're moving to start of the file. Each time you do
# # f.readline(), you're reading a line from the file and moving read head to right after the \n
# # that ends that file.
# # readline() scans each byte of the file until it finds a \n character, then stops reading the file to return what is
# # found so far. file f responsible for maintaining the current position in the file after each readline() call, so
# # that it will keep reading each line

# def rewind(f):
#     f.seek(0)

# print the line number and read corresponding line in file opened
# def print_a_line(line_count, f):
#     print(line_count, f.readline())
#
#
# current_file = open(input_file)
#
# print("First let's print the whole file:\n")
# print_all(current_file)
#
# print("Now let's rewind, kind of like a tape.")
# rewind(current_file)
#
# print("Let's print three lines:")
# current_line = 1
# print_a_line(current_line, current_file)
#
# current_line += 1
# print_a_line(current_line, current_file)
#
# current_line += 1
# print_a_line(current_line, current_file)

# def add(a, b):
#     a = float(input("Input value"))
#     b = float(input("Input value"))
#     print("ADDING %d + %d" % (a, b))
#     return(a+b)
#
# def subtract(a, b):
#     a = float(input("Input value"))
#     b = float(input("Input value"))
#     print("SUBTRACTING %d - %d" % (a, b))
#     return(a - b)
#
# def multiply(a, b):
#     a = float(input("Input value"))
#     b = float(input("Input value"))
#     print("MULTIPLYING %d * %d" % (a, b))
#     return(a * b)
#
# def divide(a, b):
#     a = float(input("Input value"))
#     b = float(input("Input value"))
#     print("DIVIDING %d / %d" % (a, b))
#     return(a / b)
#
# print("Let's do some math with just functions!")
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
#
# # A puzzle for the extra credit, type it in anyway
# print("Here is a puzzle")
#
# what = add(age, subtract(height, multiply(weight, divide(iq,2))))
# print("That becomes: ", what, "Can you do it by hand?")

# print("Let's practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """
#
# print("-----------------")
# print(poem)
# print("-----------------")
#
# five = 10 - 2 + 3 - 6
# print("This should be five: %s" % five)
#
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return (jelly_beans, jars, crates)
#
# start_point = 10000
# beans, jars, crates = secret_formula(start_point)
#
# print("With a starting point of: %d" %start_point)
# print("We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates))
#
# start_point = start_point / 10
#
# print("We can also do that this way:")
# print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

# def break_words(stuff):
#     """This function will break up words for us. """
#     words = stuff.split(' ')
#     return(words)
#
# def sort_words(words):
#     """Sorts the words."""
#     return(sorted(words))
#
# def print_first_word(words):
#     """Prints the first word after popping it off."""
#     word = words.pop(0)
#     print(word)
#
# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print(word)
#
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)
#
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# def print_first_and_last_sorted(sentence):
#     """Sorts the words and then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# # help(Test)
# # help(Test.break_words)
# # from Test import *

# def break_words(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ')
#     return words
#
# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)
#
# def print_first_word(words):
#     """Prints the first word after popping it off."""
#     word = words.poop(0)
#     print(word)
#
# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print(word)
#
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)
#
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
#
# print("Let's practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explantion
# \n\t\twhere there is none.
# """
#
#
# print("--------------")
# print(poem)
# print("--------------")
#
# five = 10 - 2 + 3 - 5
# print("This should be five: %s" % five)
#
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates
#
#
# start_point = 10000
# beans, jars, crates = secret_formula(start_point)
#
# print("With a starting point of: %d" % start_point)
# print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))
#
# start_point = start_point / 10
#
# print("We can also do that this way:")
# print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))
#
#
# sentence = "All god\tthings come to those who weight."
#
# # words = ex25.break_words(sentence)
# # sorted_words = ex25.sort_words(words)
# #
# # print_first_word(words)
# # print_last_word(words)
# # print_first_word(sorted_words)
# # print_last_word(sorted_words)
# # sorted_words = ex25.sort_sentence(sentence)
# # print(sorted_words)
# #
# # print_first_and_last(sentence)
# #
# # print_first_and_last_sorted(senence)

"""
and
or
not
!=
==
>=
<=
True
False\

True or False: True
True or True: True
False or True: True
False or False: False
True and False: False
True and True: True
False and True: False
False and False: False
not(True or False): False
not(True or True): False
not(False or True): False
not(False or False): True
not(True and False): True
not(True and True): False
not(False and True): True
not(False and False): True
"""
#
# """
# True
# False
# False
# True
# True
# True
# False
# True
# False
# False
# True
# False
# True
# False
# False
# False
# True
# True
# False
# False
# """
#
# print(3==3 and not ("testing" == "testing" or "Python" == "Fun"))
# print("chunky" == "bacon" and not(3==4 or 3==3))
# print(1==1 and not("testing" == 1 or 1 == 0))
# print(not("testing" == "testing" and "Zed" == "Cool Guy"))

# people = 40
# cars = 40
# buses = 15
#
# if cars > people:
#     print("We should take the cars.")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide.")

# print("You enter a dark room with two doors. Do you go through #1 or door #2?")
# door = input("> ")
# if door == "1":
#     print("There's a giant bear here eating a cheese cake. What do you do?")
#     print("1. Take the cake.")
#     print("2. Scream at the bear.")
#
#     bear = input(" >")
#
#     if bear == "1":
#         print("The bear eats your face off. Good job!")
#     elif bear == "2":
#         print("The bear eats your legs off. Good job!")
#     else:
#         print("Well, doing %s is probably better. Bear runs away." %bear)
#
# elif door == "2":
#     print("You stare into the endless abyss at Cthulhu's retaina.")
#     print("1. Blueberries.")
#     print("2. Yellow jacket clothespins.")
#     print("3. Understanding revolvers yelling melodies.")
#
#     insanity = input("> ")
#
#     if insanity ==  "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello. Good job!")
#     else:
#         print("The insanity rots your eyes into a pool of muck. Good job!")
#
# else:
#     print("You stumble around and fall on a knife and die. Good job!")

## check if number between a range of numbers: x in range(1,10) or 0 < x < 10 or 1 <= x < 10

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = ['1', 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

# for number in the_count:
#     print("This is count %d" % number)
#
# # same as above
# for fruit in fruits:
#     print("A fruit of type %s" % fruit)
#
# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print("I got a %r" % i)
#
# # we can also build lists, first start with an empty one
# elements = []
#
# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print("Adding %d to the list." % i)
#     # append is function that lists understand
#     elements.append(i)
#
# # now we can print them out too
# for i in elements:
#     print("Element was: %d" % i)
#
# ## list. {append, clear, copy, count, extend, index,insert, pop, remove, reverse, sort}

# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

# def numbers(a, b):
#     box = []
#     i = 0
#     while i < a:
#         box.append(i)
#         i+=b
#     print("These are your numbers:", box)

# def numbers(a):
#     box = []
#     for i in range (0, a):
#         box.append(i)
#     print("These are your numbers:", box)
#
# numbers(5, 3)

## ordinal == ordered, 1st; cardinal == cards at random, 0.

# import random
# my_randoms = random.sample(range(78), 10)
# print(my_randoms)
# print(my_randoms[4])

# from sys import exit
#
# def gold_room():
#     print("This room is full of gold. How much do you take?")
#
#     next = input("> ")
#     if int(next)==True:
#         how_much = int(next)
#     else:
#         dead("Man, learn to type a number.")
#
#     if how_much < 50:
#         print("Nice, you're not greedy, you win!")
#         exit(0)
#     else:
#         dead("You greedy bastard!")
#
# def bear_room():
#     print("There is a bear here.")
#     print("The bear has a bunch of honey.")
#     print("The fat bear is in front of another door.")
#     print("How are you going to move the bear?")
#     bear_moved = False
#
#     while True:
#         next = input("> ")
#
#         if next == "take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif next == "taunt bear" and not bear_moved:
#             print("The bear has moved from the door. You can go through it now.")
#             bear_moved = True
#         elif next == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif next == "open door" and bear_moved:
#             gold_room()
#         else:
#             bear_room()
#
# def cthulhu_room():
#     print("Here you see the great evil Cthulhu.")
#     print("He, it, whatever stares at you and you go insane.")
#     print("Do you flee for your life or eat your head?")
#
#     next = input("> ")
#
#     if "flee" in next:
#         start()
#     elif "head" in next:
#         dead("Well that was tasty!")
#     else:
#         cthulhu_room()
#
# def dead(why):
#     print(why, "Good job!")
#     exit(0)
#
# def start():
#     print("You are in the dark room.")
#     print("There is a door to your right and left.")
#     print("which one do you take?")
#
#     next = input("> ")
#
#     if next == "left":
#         bear_room()
#     elif next == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve.")
#
# start()

# next = input("> ")
# if next.isdigit():
#     how_much = int(next)
#     print("Yay! You win!")
# else:
#     print("Man, learn to type a number.")

## infinite loop: while True
## on many operating systems, program can abort with exit(0)

## never nest if-statements more than two deep and always try to do them one deep.
## if put an if in an if, then you should be looking to move that second if into another function
## boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function
## and use a good name for the variable.
## use while-loop only to loop forever
## use a for-loop for all other kinds of looping
## best way to debug a program is to use print to print out values of variables at points in the program to see where
## they go wrong.
## make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run
## them. Code a little, run a little, fix a little

## keywords:
# and
# del
    # list = [1, 2, 4, 8, "bob"]
    # del list[3]
    # print(list)
# from
# not
# while
# as
# elif
# global
    # def set_globvar_to_one():
    #     global globvar
    #     globvar = 1
    # def print_globvar():
    #     print(globvar)
    # set_globvar_to_one()
    # print_globvar()
    # print(globvar)
# or
# with
    # for 2 related operations
# assert
## asserts should be used to test conditions that should never happen.
## condition we're claiming should be true at this point in the prorgam
## similar to throwing an exception if a given condition isn't true
## exceptions should be used for errors that can conceivably happen.

# class LessThanZeroException(Exception):
#     pass
#
# class variable(object):
#     def __init__(self, value=0):
#         self.__x = value
#     def __set__(self, obj, value):
#         if value < 0
#             raise LessThanZeroException('x is less than zero')
#
#         self.__x = value
#
#     def __get__(self, obj, objType):
#         return self.__x
#
# class MyClass(object):
#     x = variable()

# else
# if
# pass
# yield
    # Generator is a function that produces a sequence of results instead of a single value
#     def createGenerator():
#         mylist = range(3)
#         for i in mylist:
#             yield i*i
#
#     mygenerator = createGenerator()
#     print(mygenerator)
#     for i in mygenerator:
#         print(i)
# break
# except
# import
# print
# class

    # class Dog:
    #
    #     kind = 'canine'
    #
    #     def __init__(self, name):
    #         self.name = name
    #
    # d = Dog('Fido')
    # e = Dog('Bud')
    #
    # d.kind
    # e.kind
    #
    # print(d.name)

# exec
# eval
    # exec and eval return output; value of string expressions
# in
# raise
    # for raising own errors
    # to reraise the current exception in exception handler, so that it can be handled further
    # up the call stack
    # if something:
    #   raise Exeception('My Error!')

# continue
    # can use to skip iteration in loop
# finally
    # finally clause is always executed before leaving the try statement, whether an exception has
    # occurred or not.

    # try:
    #     raise KeyboardInterrupt
    # finally:
    #     print("Goodbye, world!")

    # can be used for closing out of a file

    # def divide(x, y):
    #     try:
    #         result = x / y
    #     except Exception as e:
    #         print(str(e))
    #     else:
    #         print("result is", result)
    #     finally:
    #         print("executing finally clause")
    #
    # divide(10,0.00001)
# is
# return
# def
# for
# lambda
# try

# Data Types:
# True
# False
# strings
# numbers
# floats
# lists

# String Escape Sequences
#  \\
# \'
# \"
# \a
# \b
# \f
# \n
# \r
# \t
# \v

# print("Just so you know 2\\2 is equal to 1. Didn\'t you know that?")
# print("Here is quotation: \"I am so happy!\"")
# print("I will not lose to you \a ever ever ever \b so don\'t you think that, \f otherwise"
#       " you will be in for a big \n SURPRISE \n \r There are so many things \t you "
#       "should know about yourself. \v One thing is that...")

# String Formats
# %d
# %i
# %o
# %u
# %x
# %X
# %e
# %E
# %f
# %F
# %g
# %G
# %c
# %r
# %s
# %%
# digit = 10
# apple = 'Hello'
# print("The number is....%%" % digit)

# Operators:
# +
# -
# *
# **
# /
# //
# %
# <
# >
# <=
# >=
# ==
# !=
# <>
# ( )
# [ ]
# { }
# @
# ,
# :
# .
# =
# ;
# +=
# -=
# *=
# /=
# //=
# %=
# **=


# ten_things = "Apples Oranges Crows Telephones Light Sugar"
# print("Wait there's not 10 things in that list, let's fix that.")
#
# stuff = ten_things.split(' ')
# print(stuff)
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# print(more_stuff)
# while len(stuff) < 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print("There's %d items now." % len(stuff))
#
# print("There we go: ", stuff)
# print("Let's do some things with stuff.")
#
# print(stuff[1])
# print(stuff[-1])
# print(stuff.pop())
# print(' '.join(stuff))
# print('#'.join(stuff[3:5]))

# import pandas as pd
# array = [['Randy', 'Bob'], ['Alice', 'Karen'], ['Harriott', 'Elzekiel'], ['Smith', 'Lancaster']]
# # print(array)
# df = pd.DataFrame(array)
# df.columns = ['First Name', 'Last Name']
#
# df['Full Name'] = df['First Name'].str.cat(df['Last Name'], sep = ' ')
# print(df)

# import pandas as pd
# df = pd.DataFrame({'First Name': ['Bob', 'Ryan', 'Lory', 'Kayden'],
#                    'Last Name': ['Barker', 'Seagull', 'Chavalle', 'Bombat'],
#                    'Earnings': [100, 200, 400, 250]})
#
# print(df)

# # create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
#
# # create a basic set of states and some cities in them
# cities = {'CA': 'San Francisco',
#           'MI': 'Detroit',
#           'FL': 'Jacksonville'}
#
# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# # print out some cities
# print('-'*10)
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])
#
# # print some states
# print('-'*10)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abbreviation is: ", states['Florida'])
#
# # do it by using the state then cities dict
# print('-'*10)
# print("Michigan has: ", cities[states['Michigan']])
# print("Florida has: ", cities[states['Florida']])
#
# # print every state abbreviation
# print('-'*10)
# for state, abbrev in states.items():
#     print("%s is abbreviated %s" % (state, abbrev))
#
# # print every city in state
# print('-'*10)
# for abbrev, city in cities.items():
#     print("%s has the city %s" % (abbrev, city))
#
# # now do both at the same time
# print('-'*10)
# for state, abbrev in states.items():
#     print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))
#
# print('-'*10)
# # safely get an abbreviation by state that might not be there
# state = states.get('Texas', None)
#
# if not state:
#     print("Sorry, no Texas.")
#
# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print("The city for the state 'TX' is: %s" %city)

# Provinces = {'British Columbia': 'BC',
#             'Alberta': 'AB',
#             'Saskatchewan': 'SK',
#             'Manitoba': 'MB',
#             'Ontario': 'ON',
#             'Quebec': 'QC'}
#
# Cities = {'BC': 'Vancouver',
#           'AB': 'Calgary',
#           'SK': 'Regina',
#           'MB': 'Winnipeg',
#           'ON': 'Toronto',
#           'QC': 'Montreal'}
# box = []
#
# for Province, abbrev in sorted(Provinces.items()):
#     box.append(abbrev)
# print(box)
#
# contain = []
# for val in sorted(Provinces.values()):
#     contain.append(Cities[val])
# print(contain)

# # can update a dictionary by adding a new entry or key-value pair, or modifying an existing entry
# # can delete dictionary elements
# # i.e.

# Cities.clear()
# del Provinces['Ontario']
# del Provinces
# print(len(Cities))
# print(Cities.copy())
    # returns shallow copy of dictionary dict
# dict.fromkeys()
    # creates a new dictionary with keys from seq and values set to value
# dict.get(key, default=)
    # for key key, returns value or default if key not in dictionary
# dict.has_key()
    # Returns true if key in dictionary dict, false o/w
# dict.keys()
# dict.items()
# dict.setdefault(key, default=None)
# dict.update(dict2)
    # adds dictionary dict 2's key-value pairs to dict
# dict.values
# ordereddict

### Object-oriented programming
# 1. Take a key=value style container
# Get something out of it by the key's name
# in case of dicationaries, the key is a string and the syntax is [key]. In the case of modules,
# the key is an identifier, and the syntax is .key. Other than that, they are nearly the same thing.

### A class is a way to take a grouping of functions and data and place htem inside a container so you can access them
### with the ' . ' (dot) operator.

# class MyStuff(object):
#
#     def __init__(self):
#         self.tangerine = "And now a thousand years between"
#
#     def apple(self):
#         print("I am classy apples!")
### classes are like "mini-modules", can import from classes = instantiate
### when you instantiate a class, what you get is called an object.

# thing = MyStuff()
# print(thing.tangerine)
# thing.apple()

# """ Sequence of events:
# 1. Python looks for MyStuff() and see that it is a class you've defined.
# 2. Python crafts an empty object with all the functions you've specified in the class using def
# 3. Python then looks to see if you made a 'magic' __init__function, and if you have, it calls that function
# to initiatlize your newly created empty object.
# 4. In the MyStuff function __init__, get extra variable self, which is the empty object Python made for me, and can
# set variables on it
# 5. Set self.tangerine to song lyric and initialized object
# 6. Python can take newly minted object and assign it to thing variable
# """

# Classes are like blueprints or definitions for creating mini modules
# instantiation is how you make one of these mini modules and import it at the same time
# resulting created mini-module is called an object and you can then assign it to a variable to work with

# class Song(object):
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
# bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])
#
# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()

# """
# class - Tells Python to make a new kind of thing.
# object - Two meanings: the most basic kind of thing, and any instance of some thing.
# instance - what you get when you tell Python to create a class
# def - how you define a function inside a class
# self - inside the functions in a class, self is a variable for the instance/object being accessed
# inheritance - the concept that one class can inherit traits from another class
# composition - concept that a class can be composed of other classes as parts, (i.e. like how cars have wheels)
# attribute - a property classes have that are from composition are usually variables
# is-a - phrase to say that something inherits from another
# has-a - phrase to say that something is composed of other things or has traits
# """
#
# """
# class X(Y) "Make a class named X that is-a Y (i.e. X inherits from Y)"
# class X(object): def __init__(self,J) "class X has-a __init__ that takes self and J parameters"
# class X(object): def M(self,J) "class X has-a function named M that takes self and J parameters"
# foo = X() "Set foo to an instance of class X."
# foo.M(J) "From foo, get the M function and call it with parameters, self, J."
# foo.K = Q = "From foo, get the K attribute and set it to Q"
# """
#
# import random
# list = list(range(0,10))
# print(list)
# random = random.shuffle(list)
# print(list)

# import modules
# import random
# from urllib import request
# import sys
#
# # url to site containing words
# WORD_URL = "http://learncodethehardway.org/words.txt"
# # empty array to hold words
# WORDS = []
#
# # dictionary containing phrases.
# PHRASES = {
#     "class %%%(%%%):":
#         "Make a class named %%% that is-a %%%.",
#     "class %%%(object):\n\tdef __init__(self, ***)":
#         "class %%% has-a __init__ that takes self and *** parameters.",
#     "class %%%(object):\n\tdef ***(self, @@@)":
#         "class %%% has-a function named *** that takes self and @@@ parameters.",
#     "*** = %%%()":
#         "Set *** to an instance of class %%%.",
#     "***.***(@@@)":
#         "From *** get the function, and call it with parameters self, @@@.",
#     "***.*** = '***'":
#         "From *** get the *** attribute and set it to '***'."
# }
#
# # do they want to drill phrases first
# PHRASE_FIRST = False
# if len(sys.argv) == 2 and sys.argv[1] == "english":
#     PHRASE_FIRST = True
#
# # load up the words from the website
# # place each word from website into array
# for word in request.urlopen(WORD_URL).readlines():
#     # returns byte object, so convert to string
#     WORDS.append(word.strip().decode('utf-8'))
#
# # function convert that takes the strings of the snippet key and its corresponding string value
# def convert(snippet, phrase):
#     # take a random sample of words equal to the number of string matches %%%
#     class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
#     # take a random sample of words equal to the number of string matches ***
#     other_names = random.sample(WORDS, snippet.count("***"))
#     results = []
#     param_names = []
#   # # loop through the number of string matches @@@ in the snippet
#     for i in range(0, snippet.count("@@@")):
#     # param_count = integer value from 1 to 3
#         param_count = random.randint(1,3)
#     # join the random sample of words and append to array
#         param_names.append(', '.join(random.sample(WORDS, param_count)))
#
#   # # returns tuple value
#     for sentence in snippet, phrase:
#     # copy slice of sentence
#         result = sentence[:]
#
#         # fake class names
#         for word in class_names:
#             result = result.replace("%%%", word, 1)
#
#         # fake other names
#         for word in other_names:
#             result = result.replace("***", word, 1)
#
#         # fake parameter lists
#         for word in param_names:
#             result = result.replace("@@@", word, 1)
#
#         results.append(result)
#     # print("Class Names: %s" % class_names)
#     # print("Other Names: %s" % other_names)
#     return results
#
# # keep going until they hit CTRL-D
# try:
# # infinite loop
#     while True:
# # grab a list of all the keys in the PHRASES dictionary and randomly shuffle them up
#         snippets = list(PHRASES.keys())
#         random.shuffle(snippets)
#
# # for each key value, find the corresponding value (i.e. phrase)
#         for snippet in snippets:
#             phrase = PHRASES[snippet]
#             question, answer = convert(snippet, phrase)
#
#             print(question)
#
#             input("> ")
#             print("ANSWER: %s\n\n" %answer)
# except EOFError:
#     print("\nBye")


# snippet = "class %%%(%%%)"
# phrase = "Make a class named %%% that is-a %%%."
# results = []
# for sentence in snippet, phrase:
#     result = sentence[:]
#
#     class_names = ['blue', 'red']
#     other_names = ['green', 'yellow']
#
#     for word in class_names:
#         result = result.replace("%%%", word, 1)
#
#     for word in other_names:
#         result = result.replace("***", word, 1)
#
# results.append(result)
# print(results)

## Animal is-a object (yes, sort of confusing) look at the extra credit
# class Animal(object):
#     pass
#
# ## Dog is a Animal
# class Dog(Animal):
#     def __init__self(self, name):
#         ## Dog has a name
#         self.name = name
# ## Cat is an Animal
# class Cat(Animal):
#     def __init__(self, name):
#         ## Cat has a name
#         self.name = name
# ## person is a object
# class Person(object):
#     def __init__(self, name):
#         ## person has a name
#         self.name = name
#         ## person has a pet of some kind
#         self.pet = None
# ## Employee is a Person
# class Employee(Person):
#     def __init__(self, name, salary):
#         ## ?? hmm what is this strange magic?
#         super(Employee, self).__init__(name)
#         ## employee has a salary
#         self.salary = salary
#
# ## rover is-a Dog
# rover = Dog("Rover")
#
# ## satan is-a Cat
# satan = Cat("Satan")
#
# ## mary is-a Person
# mary = Person("Mary")
#
# ## mary has a pet called Satan
# mary.pet = satan
#
# ## frank is an employee with salary 120000
# frank = Employee("Frank", 120000)
#

## super is a shortcut to allow you to access the base class of a derived class without have to know or type
## the base class name
## useful for acessing inherited methods that have been overridden in a class.

## basic object-oriented analysis and design:
## write or draw about the problem
## extract key concept sfrom #1 and research them
## create a class hierarchy and object map for othe concepts
## code the classes and a test to run them
## repeat and refine

# from sys import exit
# from random import randint
#
# class Scene(object):
#     def enter(self):
#         print("This scene is not yet configured. Subclassit and implement enter().")
#         exit(1)
#
# class Engine(object):
#
#     def __init__(self, scene_map):
#         self.scene_map = scene_map
#
#     def play(self):
#         current_scene = self.scene_map.opening_scene()
#
#         while True:
#             print("\n-------")
#             next_scene_name = current_scene.enter()
#             current_scene = self.scene_map.next_scene(next_scene_name)
#
# class Death(Scene):
#     quips = [
#         "You died. You kinda suck at this.",
#         "Your mom would be proud...if she were smarter.",
#         "Such a loser.",
#         "I have a small puppy that's better at this."
#     ]
#
#     def enter(self):
#         print(Death.quips[randint(0, len(self.quips)-1)])
#         exit(1)
#
# class CentralCorridor(Scene):
#     def enter(self):
#         pass
#
# class LaserWeaponArmory(Scene):
#     def enter(self):
#         pass
#
# class TheBridge(Scene):
#     def enter(self):
#         pass
#
# class EscapePod(Scene):
#     def enter(self):
#         pass
#
# class Map(object):
#     def __init__(self, start_scene):
#         pass
#
#     def next_scene(self, scene_name):
#         pass
#
#     def opening_scene(self):
#         pass
#
# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()
#
#
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name: ", self.name, ", Salary: ", self.salary)
#
# "This would create first object of Employee Class"
# emp1 = Employee("Zara", 2000)
# "This would create second object of Employee Class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee: %d" % Employee.empCount)
# emp1.age = 7
# emp2.age = 8
# del emp1.age
#
# print(hasattr(emp1, 'age')) # Returns true if 'age' attribute exists
# print(getattr(emp2, 'age')) # Returns value of 'age' attribute
# setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
# delattr(emp1, 'age') # Delete attribute 'age'

# Built-In Class Attributes:

# Every Python class keeps following built-in attributes and they can be accessed using dot
# operator like any other attribute -

# __dict__: Dictionary containing the class's namespace
# __doc__: Class documentation string or none, if undefined
# __name__: Class name
# __module__: Module name in which the class is defined. The attribute is "__main__" in interactive mode.
# __bases__: a possibly empty tuple containing the base classes, in the order of their occurrence
# in the base class list.

# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# destroying objects (garbage collection)
# python deletes unneeded objects (built-in types or class instances) automatically to free
# the memory space. Process by which Python reclaims blocks of memory that no longer are in
# use is termed Garbage Collection

# Garbage collector runs during program execution and is triggered when an object's reference
# count reaches zero. An object's reference count changes as the number of aliases that point
# to it changes.

# An object's reference count increases when it is assigned a new name or placed in a
# container (list, tuple, or dictionary). The object's reference count decreases when it's
# deleted w/ del, its reference is reassigned, or its reference goes out of scope.
# When an object's reference count reaches zero, Python collects it automatically.

# A class can implement the special method __del__(), called a destructor, that is invoked
# when the instance is about to be destroyed. This method might be used to clean up
# any non memory resources used by an instance.

# class Point:
#         def __init__(self, x=0, y=0):
#             self.x = x
#             self.y = y
#
#         def __del__(self):
#             class_name = self.__class__.__name__
#             print(class_name, "destroyed")
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))
# del pt1
# del pt2
# del pt3

# Instead of starting from scratch, can create a class by deriving it from a preexisting
# by listing the parent class in parentheses after the new class name
# the child class inherits attributes of parent class

#class SubClassName(ParentClass1[, ParentClass2, ...]):
#'Optional class documentation string'
#class_suite

# class Parent:   # define parent class
#     parentAttr = 100
#     def __init__(self):
#         print("Calling parent constructor")
#
#     def parentMethod(self):
#         print("Calling parent method")
#
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print("Parent attribute :", Parent.parentAttr)
#
# class Child(Parent): # define child class
#     def __init__(self):
#         print("Calling child constructor")
#
#     def childMethod(self):
#         print("Calling child method")
#
#
# c = Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()

# class A: # define class A
# class B: # defined class B
# class C(A, B) # subclass of A and B

# use issubclass() or isinstance() functions to check relationships of 2 classes/instances
# issubclass(sub, sup) boolean funciton returns true if given subclass sub indeed a
# subclass sup.
# insinstanace(obj, class) boolean function returns true if obj. is an instance
# of class Class or an instance of subclass of class.


# Overriding Methods
# can override parent class method for special or different functionality

# class Parent: # define parent class
#     def myMethod(self):
#         print("Calling parent method")
#
# class Child(Parent): # define child class
#     def myMethod(self):
#         print("Calling child method")
#
# c= Child() # instance of child
# c.myMethod() # child calls overridden method

# Base Overloading Methods:
# __init__(self[,args...])     constructor (with any optional arguments);
                            #  sample call: obj = className()
#
# __del__(self)                destructor, deletes an object;
                            #  sample call: del obj
# __repr__(self)            #  __repr__(self);
                            # evaluatable string representation
                            # sample call: repr(obj)
# __str__(self)             # printable string representation
                            # sample call: str(obj)
# __cmp__(self, x)          # object comparison
                            # sample call: cmp(obj, x)

# class Vector:
#         def __init__(self, a, b):
#             self.a = a
#             self.b = b
#
#         def __str__(self):
#             return 'Vector (%d, %d)' % (self.a, self.b)
#
#         def __add__(self, other):
#             return(Vector(self.a + other.a, self.b + other.b))
#
# v1 = Vector(2,10)
# v2 = Vector(5, -2)
# print(v1+v2)

# data hiding
# an object's attribute may not be visible outside the class definition. Name
# attributes with a double underscore prefix

# class JustCounter:
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print(self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# # print(counter.__secretCount)

        ## python protects those members by internally changing the name to include the
        # class name. You can access such attributes as object.className__attrName
# print(counter._JustCounter__secretCount)

### Regular Expressions
# re.match(pattern, string, flags=0)

# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#     print("matchObj.group(): ", matchObj.group())
#     print("matchObj.group(1): ", matchObj.group(1))
#     print("matchObj.group(2): ", matchObj.group(2))
# else:
#     print("No Match!!")

# search function
# re.search(patter, string, flags=0)
# retunrs a match object on success, non on failure

# import re
# line = "Cats are smarter than dogs"
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
# if searchObj:
#     print("searchObj.group(): ", searchObj.group())
#     print("searchObj.group(1): ", searchObj.group(1))
#     print("searchObj.group(2): ", searchObj.group(2))
# else:
#     print("Nothing Found")


# match checks for match only at beginning of string.
# search checks for match anywhere in string
# import re
# line = "Cats are smarter than dogs";
# matchObj = re.match(r'dogs', line, re.M|re.I)
#
# if matchObj:
#     print("match --> matchObj.group(): ", matchObj.group())
# else:
#     print("No match!!")
#
# searchObj = re.search(r'dogs', line, re.M|re.I)
# if searchObj:
#     print("Search --> SearchObj.group() : ", searchObj.group())
# else:
#     print("Nothing Found!")

### search and replace
#re.sub(pattern, repl, string, max=0)

# import re
# phone = '2004-959-559 # This is Phone Number'
#
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print("Phone number is: ", num)
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print("Phone Number is: ", num)

# Regular Expression Modifiers: Option Flags
# optional modifier to control various aspects of matching
# re.I - case insensitive matching
# re.L - interprets words according to current locale.
# re.M - makes $ match the end of a line ( not just at end of string) and makes ^
#        match start of any line ( not just start of string)
# re.S - Makes a period match any character, including newline
# re.U - inteprets letters according to unicode character set
# re.X - permits "cuter" regular expression syntax. Ignores whitespace (except
#        inside a set {} or when escaped by a backslash) and treats unescaped # as comment marker.

# Regular Expression Patterns
# ^ - match beginning of line
# $ - match end of line
# . - match any single character except newline (using m option allows it to match newline)
# [...] - matches any single character in brackets
# [^...] - matches any single character not in brackets
# re* - matches 0 or more occurrences of preceding expression.
# re+ - matches 1 or more occurrence of preceding expression.
# re? - matches 0 or 1 occurrence of preceding expression
# re{ n} - matches exactly n number of occurrences of preceding expression.
# re{ n,} - matches n or more occurences of preceding expression.
# re{ n, m} - matches at least n and at msot m occurrences of preceding expression.
# a| b - matches either a or b
# (re) - groups regular expression sand remembers matched text
# (?imx) - temporarily toggles on i, m, or x options within a regular expression. Only that
        # area in parenthesis is affected.
# (?-imx) - temporariliy toggles off i, m or x options within a regular expression.
        # only area in parenthesis affected.
# (?: re) - groups regular expressions without remembering matched text
# (?imx: re) - temporarily toggles on i, m, or x options within parentheses
# (?imx: re) - temporarily toggles off i, m or x options within parentheses
# (?#..) - comment.
# (?=re) - specifies position using a pattern. Doesn't have a range
# (?! re) - specifies position using pattern negation. Doesn't have a range.
# (?> re) - matches independent pattern without backtracking
# \w - matches word characters
# \W - matches nonword characters
# \w - matches whitespace
# \S - matches nonwhitespace
# \d - matches digits
# \D - matches nondigits
# \A - matches beginning of string
# \Z - matches end of string. If newline exists, matches just before newline
# \z - matches end of string
# \G - matches point where last match finished
# \b - Matches word boundaries when outside brackets. Matches backspace(0x08) when
    #  inside brackets.
# \B - matches nonword boundaries
#\n, \t, etc. - matches newlines, carriage returns, tabs, etc.
#\1...\9 - matches nth grouped subexpression
#\10 - matches nth grouped subexpression if it matched already.

### character classes:
# [Pp]ython - match "python" or "Python"
# rub[ye] - match "ruby" or "rube"
# [aeiou] - match any one lowercase vowel
# [0-9] - match any digit
# [a-z] - match any lowercase letter
# [A-Z] - match any uppercase letter
# [a-zA-Z0-9] - match any of th eabove
# [^aeiou] - match anything other than lowercase vowel
# [^0-9] - match anyting other than a digit

### repetition cases
# ruby? - match "rub" or "ruby"
# ruby* - match 'rub' plus 0 or more y's
# ruby+ - match 'rub' plus 1 or more y's
# \d{3} - match exactly 3 digits
# \d(3,} - match exactly 3 or more digits
# \d{3,5} - match 3,4, or 5 digits

### Non-greedy repetitions
# <.*> - matches "<python>perl>"
# <.*?> - matches "<python>" in "<python>perl"

### Grouping with Parentheses
# \D\d+ - no group + repeats \d
# (\D\d)+ - grouped: + repeats \D\d pair
# ([Pp\ython(,)?)+ - match "Python", "Python, python, python", etc.

### Alternatives
# python|perl - match python or perl
# rub(y|le) - match ruby or ruble
# Python(!+|\?) - "python" followed by one or more ! or one ?

# import os
# os.rename("test1.txt", "test2.txt") # rename a file from test1.txt to test2.txt
# os.remove(file_name)

### directories in Pythong
# mkdir - create directories in current directory
# os.mkdir("newdir")
# os.chdir("newdir")  # change current directory
# os.chdir("home/newdir")

# os.getcwd()  # get current location of directory
# os.rmdir('/tmp/test') # deletes directory

# implicit inheritance
# class Parent(object):
#         def implicit(self):
#             print("PARENT IMPLICIT()")
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# # Override explicitly
#
# class Parent(object):
#     def override(self):
#         print("PARENT OVERRIDE()")
#
# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()

# Alter Before or After

# class Parent(object):
#         def altered(self):
#             print("PARENT altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
# dad.altered()
# son.altered()

# class Parent(object):
#     def override(self):
#         print("PARENT override()")
#
#     def implicit(self):
#         print("PARENT implicit()")
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()

### Reason for Super:
# Multiple Inheritance - when you define a class that inherits from one or more classes
# class SuperFun(Child, BadStuff):
# pass
# Whenever have implicit ations on any SuperFun instance, Python has to look up possible function
# in class hierarchy for both Child and Badstuff
# Use super instead

### Using super() with __init__
# class Child(Parent):
#
#     def __init__(self, stuff):
#         self.stuff = stuff
#         super(Child, self).__init__()  ## se4tting some variables in the __init__ before having
                                         ## the parent initialize with its Parent.__init__



# ### Composition
# # Use other classes and modules rather than rely on implicit inheritance.
#
# class Other(object):
#     def override(self):
#         print("OTHER override()")
#     def implicit(self):
#         print("OTHER implicit()")
#     def altered(self):
#         print("OTHER altered()")
#
# class Child(object):
#     def __init__(self):
#         self.other = Other() # implcit call, composition
#
#     def implicit(self):
#         self.other.implicit() # implcit call, composition
#
#     def override(self):
#         print("CHILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE OTHER altered()")
#         self.other.altered()
#         print("CHILD, AFTER OTHER altered()")
#
# # there is not a parent-child is-a relationship. It's a has-a relationship where child has-a
# # Other that it uses to get its work done.
#
# son = Child()
# son.implicit()
# son.override()
# son.altered()
#
# path = 'pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
# open(path).readline
#
# import json
# path = 'pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
# records = [json.loads(line) for line in open(path)]
# # # print(records[0]['tz'])
# # # print(records[0]['g'])
# # time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# # # print(time_zones)
# #
# # # get counts by time zone:
# #
# # def get_counts(sequence):
# #     # get counts from a list feeded in
# #     counts = {}
# #     for x in sequence:
# #         if x in counts:
# #             counts[x] +=1
# #         else:
# #             counts[x] = 1
# #     return counts
# #
# # from collections import defaultdict
# #
# # def get_counts2(sequence):
# #     counts = defaultdict(int) # values will initialize to 0
# #     for x in sequence:
# #         counts[x] += 1
# #     return counts
# #
# # counts = get_counts(time_zones)
# # # print(counts)
# # # print(counts['America/New_York'])
# # # print(len(time_zones))
# #
# # def top_counts(count_dict, n=10):
# #     value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
# #     value_key_pairs.sort()
# #     return value_key_pairs[-n:]
# #
# # print(top_counts(counts, 20))
# #
# # from collections import Counter
# # # count frequency of each item in list
# # counts = Counter(time_zones)
# # print(counts.most_common(10))
#
# ### counting time zones with pandas:
# import pandas as pd
# frame = pd.DataFrame(records)
# # print(frame.head())
# # print(frame['tz'][:10])
# # tz_counts = frame['tz'].value_counts()
# # print(tz_counts)
# # clean_tz = frame['tz'].fillna('Missing')
# # clean_tz[clean_tz == ''] = 'Unknown'
# # tz_counts = clean_tz.value_counts()
# # print(tz_counts[:10])
#
#
# # import matplotlib.pyplot as plt
# # tz_counts[:10].plot(kind='barh', rot=0)
# # plt.show()
#
# import re
# # results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# # print(results.value_counts()[:8])
#
# # decompose top time zones into Windows and non-Windows users
# # remove nulls
# cframe = frame[frame.a.notnull()]
# # compute a value whether each row is Windows or not
#
# import numpy as np
# # use np.where to transform series
# operating_system = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
# # print(operating_system[:5])
#
#
# # can group data by time zone column and new list of operating system
# by_tz_os = cframe.groupby(['tz', operating_system])
# # reshape into table
#
# agg_counts = by_tz_os.size().unstack().fillna(0)
# # print(agg_counts[:10])
#
# # select top overall time zones
# # construct an indirect index array from row counts
# # print(agg_counts)
# indexer = agg_counts.sum(1).argsort()
# # print(indexer[:10])
#
# ## use take to select the rows in that order, slice off last 10 rows
# count_subset = agg_counts.take(indexer)[-10:]
# # print(count_subset)
#
# import matplotlib.pyplot as plt
# # count_subset.plot(kind='barh', stacked=True)
#
# normed_subset = count_subset.div(count_subset.sum(1), axis=0)
# # print(normed_subset)
# normed_subset.plot(kind = 'barh', stacked=True)
# plt.show()

## MovieLens 1M Data Set
# import pandas as pd
# directory = 'pydata-book-master/ch02/movielens/'
#
# unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
# users = pd.read_table(directory+'users.dat', sep='::', header=None, names=unames)
#
# rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
# ratings = pd.read_table(directory+'ratings.dat', sep='::', header=None, names=rnames)
#
# mnames = ['movie_id', 'title', 'genres']
# movies = pd.read_table(directory+'movies.dat', sep='::', header=None, names=mnames)
#
# # print(users.head())
# # print(ratings.head())
# # print(movies.head())
#
# data = pd.merge(pd.merge(ratings, users), movies)
# # print(data.ix[0])
#
# # aggregate ratings grouped by one or more user or movie attributes
# # get mean movie ratings for each film grouped by gender.
# # use pivot table
# # print(data.head())
# mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# # print(mean_ratings.head())
#
# # filter down to movies that received 250 ratings -> get series of group sizes
# ratings_by_title = data.groupby('title').size()
# # print(ratings_by_title.sort_values())
# active_titles = ratings_by_title.index[ratings_by_title >= 250]
# # print(active_titles)
#
# # index of titles receiving at least 250 ratings can be used to select rows from mean_ratings pivot table
# mean_ratings = mean_ratings.ix[active_titles]
# # print(mean_ratings)
#
# # sort top films among female viewers, descending order
# top_female_ratings = mean_ratings.sort_index(by = 'F', ascending = False)
# # print(top_female_ratings[:10])
#
# ### Measuring rating disagreement
# # find movies most divisive between male and female viewers.
#
# mean_ratings['diff'] = abs(mean_ratings['M'] - mean_ratings['F'])
# sorted_by_diff = mean_ratings.sort_index(by='diff', ascending = False)
# # print(sorted_by_diff[:15])
# # print(sorted_by_diff[:15])
#
# # reverse order of rows and slice off top 15 rows -> get movies preferred by men that women didn't rate as highly
# # sorted_by_diff[::-1][:15]
#
# # movies that elicited most disagreement among viewers independent of gender --> variance, std dev
# # group titles and then use std dev
# ratings_std_by_title = data.groupby('title')['rating'].std()
# # print(ratings_std_by_title)
# ## filter down to active titles
# ratings_std_by_title = ratings_std_by_title.ix[active_titles]
# print(ratings_std_by_title.order(ascending=False)[:10])


### US Baby Names 1880-2010

# import pandas as pd
# # names1880 = pd.read_csv('pydata-book-master/ch02/names/yob1880.txt', names = ['name', 'sex', 'births'])
# # # print(names1880)
# #
# # print(names1880.groupby('sex').births.sum())
#
# years = range(1880, 2011)
# pieces = []
# columns = ['name', 'sex', 'births']
#
# for year in years:
#     path = 'pydata-book-master/ch02/names/yob%d.txt' %year
#     frame = pd.read_csv(path, names=columns)
#     frame['year'] = year
#     pieces.append(frame)
#     names = pd.concat(pieces, ignore_index = True)
# # concat glues the dataframe objects together row-wise by default.
# # pass ignore_index = True because not interested in preserving original row numbers
#
# # print(names)
# # aggregate the data at the year and sex level
# total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# # print(total_births)
#
# # import matplotlib.pyplot as plt
# # total_births.plot(title = 'Total births by sex and year')
# # plt.show()
#
# # insert column prop with fraction of babies given each name relative to total number of births
# def add_prop(group):
#     # integer division floors
#     births = group.births.astype(float)
#
#     group['prop'] = births / births.sum()
#     return group
#
# names = names.groupby(['year', 'sex']).apply(add_prop)
# # print(names)
#
# # use np.allclose to check that group sums are sufficiently close to 1
# import numpy as np
# # print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))
#
# # extract subset of the data to facilitate further analysis: top 1000 names for each
# # sex/year combination.
# def get_top1000(group):
#     return group.sort_index(by = 'births', ascending = False)[:1000]
#
# grouped = names.groupby(['year', 'sex'])
# top1000 = grouped.apply(get_top1000)
# # print(top1000)
#
# # other approach:
# # pieces = []
# # for year, group in names.groupby(['year', 'sex']):
# #     pieces.append(group.sort_index(by='births', ascending = False)[:1000])
# # top1000 = pd.concat(pieces, ignore_index=True)
# # print(top1000)
#
# # boys = top1000[top1000.sex == 'M']
# # # # print(boys)
# # # # print(boys.groupby(['year']).prop.sum())
# # girls = top1000[top1000.sex == 'F']
# # print(girls)
#
# # Form a pivot table of the total number of births by year and name:
# # total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
# # # print(total_births)
# #
# # subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# # import matplotlib.pyplot as plt
# # subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year")
# # plt.show()
#
# # Measuring increase in naming diversity
# # measure proportion of births represented by to 1000 most popular names, aggregated and plotted by
# # year and sex
#
# # table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# # print(table)
# # import matplotlib.pyplot as plt
# # table.plot(title="Sum of table1000.prop by year and sex", yticks=np.linspace(0,1.2, 13),
# #            xticks=range(1880, 2020, 10))
# # plt.show()
# # shows that there is increasing name diversity (decreasing total proportion in top 1000)
# # df = boys[boys.year == 2010]
# # print(df)
#
# # after sorting prop in descending order, how many of the most popular names it takes to reach 50%.
# # prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
# # print(prop_cumsum)
# # import matplotlib.pyplot as plt
# # prop_cumsum.plot()
# # plt.show()
#
# # print(prop_cumsum.searchsorted(0.5))
#
# ## in 1990 this number was smaller
# # df = boys[boys.year==1990]
# # in1990 = df.sort_index(by='prop', ascending=False).prop.cumsum()
# # print(in1990.searchsorted(0.5))
#
# # can apply operation to each year/sex combination, return count for each group
#
# # def get_quantile_count(group, q = 0.5):
# #     group = group.sort_index(by='prop', ascending=False)
# #     return group.prop.cumsum().searchsorted(q) + 1
# #
# # diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count).unstack('sex')
# # # print(diversity)
# # import matplotlib.pyplot as plt
# # diversity.plot(title="Number of popular names in top 50%")
# # plt.show()
# # girl names more diverse than boy names
#
# ## "Last Letter" Revolution
# # aggregate all of the births in full data set by year, sex and final letter
# # get_last_letter = lambda x: x[-1]
# # last_letters = names.name.map(get_last_letter)
# # last_letters.name = 'last_letter'
# #
# # table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)
#
# # select out three representative years spanning the history
# # subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# # print(table)
# # print(subtable)
#
# # normalise table by total births to compute new table containing proportion of total births for each
# # sex ending in each letter:
#
# # subtable.sum()
# # letter_prop = subtable / subtable.sum().astype(float)
# # import matplotlib.pylab as plt
# # fig, axes = plt.subplots(2, 1, figsize = (10,8))
# # letter_prop['M'].plot(kind='bar', ax=axes[0], title='Male')
# # letter_prop['F'].plot(kind='bar', ax=axes[1], title='Female', legend=False)
# # plt.show()
#
# # normalize by year and sex and select subset of letters for the boy names
# # transpose to make each column a time series
# # letter_prop = table / table.sum().astype(float)
# # dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
# # # print(dny_ts.head())
# # import matplotlib.pyplot as plt
# # dny_ts.plot(title="proportion of boy names ending with d, n, y")
# # plt.show()
#
# ### Boy names that became girl names (and vice-versa)
# all_names = top1000.name.unique()
# mask = np.array(['lesl' in x.lower() for x in all_names])
# lesley_like = all_names[mask]
# # print(lesley_like)
#
# # filter down to just those names and sum births grouped by name
# filtered = top1000[top1000.name.isin(lesley_like)]
# # print(filtered)
# # print(filtered.groupby('name').births.sum())
#
# ## aggregate by sex and year and normalize within year:
# table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
# table = table.div(table.sum(1), axis=0)
# print(table)
# import matplotlib.pyplot as plt
# table.plot(style={'M': 'k-', 'F': 'k--'})
# plt.show()

# def function1(x, y, z):
#     return (x+y) / z
#
# a = 5
# b = 6
# c = 7.5
#
# result = function1(a, b, c)

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#
#     x, y = inst.args
#     print('x=', x)
#     print('y=', y)

# user-defined exceptions

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value=', e.value)

# basket = ['apple', 'orange', 'apple']
# for f in sorted(set(basket)):
#     print(f)

import numpy as np
import math

# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

# filtered_data = []
# for value in raw_data:
#     if not np.isnan(value):
#         filtered_data.append(value)

# filtered_data = [value for value in raw_data if not np.isnan(value)]

# filtered_data = filter(lambda x: np.isnan(x) == False, raw_data)
#
# print(list(filtered_data))

import numpy
#
# matrix = [
#     [1, 2, 3, 1],
#     [5, 6, 7, 2],
#     [8, 9, 10, 3]
# ]
#
# # print([[row[i] for row in matrix] for i in range(3)])
#
# array = np.array(matrix)
# print(array.T)

# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
#
# print({x: x**2 for x in (2, 4, 6)})

# dict(sape = 4139, guido = 4127)
#
# for i, v in enumerate(['tic', 'tac', 'tac']):
#     print(i, v)

import pandas as pd
import numpy as np
import itertools
import functools
import datetime as dt

# df = pd.DataFrame({'AAA': [4, 5, 6, 7],
#                    'BBB': [10, 20, 30, 40],
#                    'CCC': [100, 50, -30, -50]})

# df.ix[df.AAA >= 5, 'BBB'] =- 1
# df.ix[df.AAA < 5, ['BBB', 'CCC']] = 2000
# df.ix[df.AAA >= 5, ['BBB', 'CCC']] = 555
#
# print(df)

# df_mask = pd.DataFrame({'AAA': [True]*4, 'BBB': [False]*4, 'CCC': [True, False]*2})
#
# df = df.where(df_mask, -1000)
# df['logic'] = np.where(df.AAA > 5, 'high', 'low')
# print(df)

# df2 = df.ix[(df['BBB'] < 25) &
#             (df['CCC'] >= -40), ['AAA', 'BBB', 'CCC']]
# print(df)
# print('---'*10)
# print(df2)

# df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA' ] = 0.1
# print(df)

# aValue = 43
#
# df = df.ix[(np.abs(df.CCC-aValue)).argsort()]
# print(df)
# import functools
# crit1 = df.AAA <= 5.5
# crit2 = df.BBB == 10.0
# crit3 = df.CCC > -40
#
# critlist = [crit1, crit2, crit3]
#
# allcrit = functools.reduce(lambda x, y : x & y, critlist)
#
# print(df[allcrit])


# rng = pd.date_range('1/1/2013', periods=100, freq='D')
# data = np.random.randn(100,4)
# cols = ['A', 'B', 'C', 'D']
# df1, df2, df3 = pd.DataFrame(data, index=rng, columns=cols), pd.DataFrame(data, index=rng, columns=cols), \
#                 pd.DataFrame(data, index=rng, columns=cols)
#
# pf = pd.Panel({'df1': df1, 'df2': df2, 'df3': df3})
# pf = pf.transpose(2,0,1)
# pf['E'] = pd.DataFrame(data, rng, cols)
# pf = pf.transpose(1,2,0)
# pf.loc[:, :, 'F'] = pd.DataFrame(data, rng, cols)

#
# rng = pd.date_range('1/1/2013', periods=10, freq='D')
# cols = ['A', 'B', 'C', 'D']
# data = np.random.randint(1,4, size=(10,4))
# df = pd.DataFrame(data, index=rng, columns=cols)
# source_cols = df.columns
# new_cols = [str(x) + "_cat" for x in source_cols]
# categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
# df[new_cols] = df[source_cols].applymap(categories.get)
#
# print(df)

# df = df.groupby('AAA')['BBB'].idxmin()
# print(df)
#
# df = pd.DataFrame({'row': [0, 1, 2],
#                    'one_x': [1.1, 1.1, 1.1],
#                    'two_x': [1.2, 1.2, 1.2],
#                    'two_y': [1.22, 1.22, 1.22]})
#
# df = df.set_index('row')
# df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])
# df = df.stack(0).reset_index(1)
# print(df)

# df = pd.DataFrame(np.random.randn(6, 1), index = pd.date_range('2013-08-01', periods=6, freq='B'),
#                   columns=list('A'))
#
# df.ix[3, 'A'] = np.nan
# df.reindex(df.index[::-1]).ffill()
# print(df)

# data = [[70+x+y+(x*y)%3 for x in range(4)] for y in range(9)]
# index = list(itertools.product(['Ada', 'Quinn', 'Violet'],
#                                ['Comp', 'Math', 'Sci']))
# headr = list(itertools.product(['Exams', 'Labs'],
#                                ['I', 'II']))
# indx = pd.MultiIndex.from_tuples(index, names = ['student', 'course'])
# cols = pd.MultiIndex.from_tuples(headr)
#
# df = pd.DataFrame(data, indx,cols)
# All = slice(None)


# df.columns = df.columns.get_level_values(0)
# df.columns = [''.join(col).strip() for col in df.columns.values]
# print(df)
# print(df.loc[(All, 'Math'), (All, 'II')])

# cols = pd.MultiIndex.from_tuples([(x, y) for x in ['A', 'B', 'C'] for y in ['O', 'I']])
# df = pd.DataFrame(np.random.randn(2, 6), index=['n', 'm'], columns=cols)
# df2 = df.div(df['C'], level = 1)
# print(df)
# print(df2)

# coords = [('AA', 'one'), ('AA', 'six'), ('BB', 'one'), ('BB', 'two'), ('BB', 'six')]
# index = pd.MultiIndex.from_tuples(coords)
# df = pd.DataFrame([11, 22, 33, 44, 55], index, ['MyData'])
#
# print(df)
# print(df.xs('BB', level=0, axis=0))
# print(df.xs('six', level=1, axis=0))

# df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
#                    'size': list('SSMMMLL'),
#                    'weight': [8, 10, 11, 1, 20, 12, 12],
#                    'adult': [False] * 5 + [True] *2})
# print(df)
# # list size of animals with highest weight
# s = df.groupby(['animal'])['weight'].idxmax()
# print(df.ix[s][['animal', 'size']])

# df2 = df.groupby('animal').apply(lambda x: x['size'].ix[x['weight'].idxmax()])
# print(df2)

# s = pd.Series([i/100 for i in range(1, 11)])
# def cumRet(x,y):
#     return x + (1+y)
#
# def Red(x):
#     return functools.reduce(cumRet, x, 1.0)
#
# s2 = s.add(1).cumprod()
# print(s)
# print(s2)
#
# s3 = pd.expanding_apply(s, lambda s: functools.reduce(lambda x, y: x*(1+y), s, 1))
# print(s3)

# replace values with mean of group

# df = pd.DataFrame({'A': [1, 1, 2, 2],
#                    'B': [1, -1, 1, 2]})
#
# mean_A = df['A'].mean()
# mean_B = df['B'].mean()
#
# gb = df.groupby('A')
#
# def replace(g):
#     mask = g < 0
#     g.loc[mask] = g[~mask].mean()
#     return g
#
# blah = gb.transform(replace)
# print(blah)

# df = pd.DataFrame({'code': ['foo', 'bar', 'baz']*2,
#                    'data': [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],
#                    'flag': [False, True]*3})
# # print(df)
# #
# # code_groups = df.groupby('code')
# # agg_n_sort_order = code_groups[['data']].transform(sum).sort_values(by='data')
# # sorted_df = df.ix[agg_n_sort_order.index]
# # print(sorted_df)
#
# mask = df.data.argsort()
# print(df.ix[mask])

# rng = pd.date_range(start="2014-10-07", periods=10, freq='2min')
# ts = pd.Series(data=list(range(10)), index=rng)
# print(ts)
#
# def MyCust(x):
#     if len(x) > 2:
#         return x[1]*1.234
#     else: return np.nan
#
# mhc = {'mean': np.mean, 'max': np.max, 'custom': MyCust}
#
# ts2 = ts.resample("5min", how = mhc)
# print(ts2)
#
#
# df = pd.DataFrame({'color': 'Red Red Red Blue'.split(),
#                    'Value': [100, 150, 50, 50]})
#
# print(df['color'].value_counts())
#
# df['counts'] = df.groupby(['color']).transform(len)
# print(df)

# df = pd.DataFrame({u'line_race': [10, 10, 8, 10, 10, 8],
#                    u'beyer': [99, 102, 103, 103, 88, 100]},
#                   index=[u'Last Gunfighter', u'Last Gunfighter', u'Last Gunfighter',
#                          u'Paynter', u'Paynter', u'Paynter'])
# df['beyer_shifted'] = df.groupby(level=0)['beyer'].shift(1)
# print(df)

# df = pd.DataFrame({'host': ['other', 'other', 'that', 'this', 'this'],
#                    'service': ['mail', 'web', 'mail', 'mail', 'web'],
#                    'no': [1, 2, 1, 2, 1]}).set_index(['host', 'service'])
#
# df = df.reset_index()
# print(df)
# mask = df.groupby(['host'])['no'].idxmax()
# df2 = df.ix[mask]
# print(df2)

# mask = df.groupby(level=0).agg('idxmax')
# df_count = df.loc[mask['no']].reset_index()
# print(df_count)

# df = pd.DataFrame([0, 1, 0, 1, 1, 1, 0, 1, 1], columns=['A'])
# print(df)
#
# print(df.A.groupby((df.A != df.A.shift()).cumsum()).groups)
# print(df.A.groupby((df.A != df.A.shift()).cumsum()).cumsum())

# df = pd.DataFrame({'basket': [88, 88, 88, 123, 477, 477, 566],
#                    'sale': [15, 30, 16, 90, 77, 57, 90],
#                    'date': ['3-01-2012', '11-02-2012', '16-08-2012', '18-06-2012', '19-08-2012',
#                             '11-12-2012', '6-07-2012']})
# print(df)
#
# # calculate previous sale, sale count, meantodate, maxtodate
#
# from pandas import concat
# from pandas.stats.moments import expanding_mean, expanding_count
#
# def handler(grouped):
#     se = grouped.set_index('date')['sale'].sort_index()
#
#     return concat(
#         {
#             'MeanToDate': expanding_mean(se),
#             'MaxToDate': se.cummax(),
#             'SaleCount': expanding_count(se),
#             'Sale': se,
#             'PrevSale': se.shift(1)
#         },
#         axis=1
#     )
#
# new_df = df.groupby('basket').apply(handler).reset_index()
# print(new_df)

# df = pd.DataFrame({'enddate': ['2012-10-25', '2012-10-25', '2012-10-27', '2012-10-26', '2012-10-28',
#                                '2012-10-28', '2012-10-28', '2012-10-28', '2012-10-30', '2012-11-01',
#                                '2012-11-01', '2012-11-01', '2012-11-03', '2012-11-04',
#                                '2012-11-04', '2012-11-04', '2012-11-04', '2012-11-04', '2012-11-05',
#                                '2012-11-07'],
#                    'favorable': [0.48, 0.51, 0.51, 0.56, 0.48, 0.46, 0.48, 0.49, 0.53, 0.49, 0.47,
#                                  0.51, 0.49, 0.53, 0.47, 0.49, 0.52, 0.50, 0.51, 0.51],
#                    'unfavourable': [0.49, 0.48, 0.47, 0.40, 0.49, 0.46, 0.49, 0.48, 0.45, 0.49,
#                                     0.47, 0.45, 0.45, 0.39, 0.44, 0.48, 0.46, 0.47, 0.46, 0.41],
#                    'other': [0.03, 0.02, 0.02, 0.04, 0.04, 0.09, 0.03, 0.03, 0.02, 0.03, 0.05, 0.04,
#                              0.06, 0.00, 0.08, 0.03, 0.01, 0.03, 0.02, 0.00]}).set_index('enddate')
#
# df.index = pd.to_datetime(df.index)
# # print(df)
#
# blah = df.resample("1d", how={'favorable': np.mean, 'other': np.mean, 'unfavourable': np.mean}).fillna(0)
# blah2 = pd.rolling_mean(blah, window=3, min_periods=1)
# print(blah)
# print(blah2)

# df = pd.DataFrame({'Case': ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A'],
#                    'Data': np.random.randn(9)})
# # print(df)

# count = 0
# ls = []
# for i in df['Case']:
#     if i == 'A':
#         ls.append(count)
#     else:
#         ls.append(count)
#         count+=1
# df['grpb'] = ls
#
# a = df.groupby('grpb')
# print(a)

# gg = list(df.groupby((df.Case == 'B').shift(1).fillna(0).cumsum()))
# print(gg)

# df['grpb'] = np.nan
# # print(df)
# breaks = df[df.Case == 'B'].index
# df['grpb'].ix[breaks] = range(len(breaks))
# df.fillna(method='bfill').fillna(len(breaks))
# print(df)

# grades = [48, 99, 75, 80, 42, 80, 72, 68, 36, 78]
#
# df = pd.DataFrame({'ID': ["x%d" % r for r in range(10)],
#                    'Gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M' ],
#                    'ExamYear': ['2007', '2007', '2007', '2008', '2008', '2008', '2008', '2009', '2009', '2009'],
#                    'Class': ['algebra', 'stats', 'bio', 'algebra', 'algebra', 'stats', 'stats', 'algebra',
#                              'bio', 'bio'],
#                    'Participated': ['yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes'],
#                    'Passed': ['yes' if x > 50 else 'no' for x in grades],
#                    'Employed': [True, True, True, False, False, False, False, True, True, False],
#                    'Grade': grades})
#
# print(df)
#
# g = df.groupby('ExamYear').agg({'Participated': lambda x: x.value_counts()['yes'],
#                             'Passed': lambda x: sum(x == 'yes'),
#                             'Employed': lambda x: sum(x),
#                             'Grade': lambda x: sum(x)/len(x)})
# print(g)
#

# df = pd.DataFrame(data={'A' : [[2,4,8,16],[100,200],[10,20,30]],
#                         'B' : [['a','b','c'],['jj','kk'],['ccc']]},index=['I','II','III'])
# # print(df)
#
# def SeriesFromSubList(aList):
#     return pd.Series(aList)
#
# df_orgz = pd.concat(dict([ (ind, row.apply(SeriesFromSubList)) for ind, row in df.iterrows() ]))
# print(df_orgz)
#
# df2 = pd.concat(dict([ (x[0],x[1].apply(lambda y: pd.Series(y))) for x in df.iterrows() ]))
# print(df2)

# tmp = pd.DataFrame(np.random.randn(2000,2)/10000, columns=['A','B'])
# tmp['date'] = pd.date_range('2001-01-01',periods=2000)
# tmp['ii'] = range(len(tmp))
#
# def gm(ii, df, p):
#     x_df = df.iloc[map(int, ii)]
#     #print x_df
#     v =((((x_df['A']+x_df['B'])+1).cumprod())-1)*p
#     #print v
#     return v.iloc[-1]
#
# #print tmp.head()
# res = pd.rolling_apply(tmp.ii, 50, lambda x: gm(x, tmp, 5))
# print(res)

# import datetime
#
# rng = pd.date_range('1/1/2000', periods=24, freq='H')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# # # print(ts)
# #
# # # include times between 9am and 6 pm (inclusive)
# # g = ts.ix[ts.index.indexer_between_time(datetime.time(9), datetime.time(18))]
# # print(g)
#
# h = ts.ix[ts.index.indexer_between_time(datetime.time(18), datetime.time(9), include_start=False,
#                                         include_end=False)]
# print(h)

# import pandas as pd
# index = pd.date_range('2013-01-01', periods=10, freq='15min')
# data=pd.DataFrame(data=np.random.randn(len(index)), columns=['value'], index=index)
# # print(data)
#
# data = data.ix[data.index.indexer_between_time('1:15', "02:00")]
# print(data)

# rng = pd.date_range('20130101 09:00', '20130110 16:00', freq='30T')
# rng = rng.take(rng.indexer_between_time('09:30', '16:00'))
# rng = rng[rng.weekday<5]
# rng.to_series()
# print(rng)

import datetime


# intervals = np.random.randint(0, 1000, size=100).cumsum()
# df = pd.DataFrame({'time': [pd.Timestamp('20140101') + pd.offsets.Milli(i) for i in intervals],
# 'value': np.random.randn(len(intervals))})
#
# pd.date_range('20140101 00:00:00', '20140101 01:00:00', freq='s')
#
# new_range = pd.date_range('20140101 00:00:00', '20140101 01:00:00', freq='s') + pd.Index(df.time)
# df.set_index('time').reindex(new_range).ffill().head(10)
# df.drop_duplicates(['time']).set_index('time').reindex(new_range).ffill().info()


# calculate first day of month
# dates = pd.date_range('2000-01-01', periods=5)
#
# dates = dates.to_period(freq='M').to_timestamp()
# print(dates)

#
# monthly_return = pd.DataFrame({'date': ['2008-07-01', '2008-08-01', '2008-09-01', '2008-10-01',
#                                         '2008-11-01', '2008-12-01', '2009-01-01', '2009-02-01',
#                                         '2009-03-01', '2009-04-01', '2009-05-01', '2009-06-01',
#                                         '2009-07-01', '2009-08-01', '2009-09-01', '2009-10-01',
#                                         '2009-11-01', '2009-12-01', '2010-01-01', '2010-02-01',
#                                         '2010-03-01', '2010-04-01', '2010-05-01', '2010-05-01',
#                                         '2010-06-01', '2010-07-01', '2010-08-01', '2010-09-01',
#                                         '2010-10-01', '2010-11-01', '2010-12-01'],
#                                'value': np.abs(np.random.randint(0,9,31)),
#                                'category': np.random.choice(['A', 'B', 'C'], 31)})
# monthly_return['date'] = pd.to_datetime(monthly_return.date)
#
# monthly_return = monthly_return.set_index(['date'])
#
# resamp = monthly_return.groupby('category').resample('M', how='sum')
# g = resamp.groupby(level = 'date').apply(lambda x: x/x.sum())
# print(g.dropna().reset_index())
#
#
# g = monthly_return.groupby(pd.TimeGrouper('6M', closed='left')).aggregate(np.sum)
# print(g)

# g = monthly_return.set_index('date').groupby(pd.TimeGrouper('6M'))['value'].apply(lambda x: x.count())
# print(g)

# g = monthly_return.set_index('date').groupby(pd.TimeGrouper('6M', closed='left')).apply(
#     lambda x: x.groupby('category').sum())
# print(g)

# g=pd.pivot_table(monthly_return, values='value', index=['date', 'category'], aggfunc=np.sum)
# print(g)

# Resampling with custom period
# begin = pd.datetime(2013, 1, 1)
# end = pd.datetime(2013, 3, 20)
# dtrange = pd.date_range(begin, end)
#
# p1 = np.random.rand(len(dtrange))+5
# p2 = np.random.rand(len(dtrange))+10
# df = pd.DataFrame({'p1': p1, 'p2': p2}, index=dtrange)
# # print(df)
#
# d = df.index.day - np.clip((df.index.day-1) // 10, 0, 2)*10 -1
# date = df.index.values - np.array(d, dtype='timedelta64[D]')
# g = df.groupby(date).mean()
#
# print(g)
# print(date)


# dates = pd.date_range('01-Jan-2014', '11-Jan-2014', freq='T')[0:-1]
# dates = dates[dates.dayofweek < 5]
#
# s = pd.TimeSeries(np.random.randn(dates.size), dates)
# g = s.groupby(lambda d: d.date()).resample('30 min')
# print(g)

# rng = pd.date_range('2001-01-01', periods=6)
# df1 = pd.DataFrame(np.random.randn(6,3), index=rng, columns=['A', 'B', 'C'])
#
# df2 = df1.copy()
# df = df1.append(df2, ignore_index=True)
# print(df)

# df = pd.DataFrame(data={'Area': ['A']*5 + ['C']*2,
#                         'Bins': [110]*2 + [160]*3 + [40] *2,
#                         'Test_0': [0, 1, 0, 1, 2, 0, 1],
#                         'Data': np.random.randn(7)})
# df['Test_1'] = df['Test_0'] -1
#
# g = pd.merge(df, df, left_on = ['Bins', 'Area', 'Test_0'], right_on = ['Bins', 'Area', 'Test_1'],
#          suffixes=('_L', '_R'))
#
# print(g)

# rng = pd.date_range('2016-01-01', periods=20)
# dfL1 = pd.DataFrame({'category1': np.random.choice(['A', 'B', 'C'], 20),
#                      'factor1': np.random.randint(1,9, 20)}, index=rng)
# dfR1 = pd.DataFrame({'category2': np.random.choice(['A', 'B', 'C'], 20),
#                      'factor2': np.random.randint(1,9, 20)}, index=rng)
#
#
# dfL1 = dfL1.set_index('category1', append=True)
# dfR1 = dfR1.set_index('category2', append=True)
#
# g = dfL1.join(dfR1)
#
# print(g)

#
# df_a = pd.DataFrame({'a': [1,2,3,4,1],
#                      'b': [4,5,6,8,7]})
#
# df_b = pd.DataFrame({'c': [2,3,2],
#                      'd': [7,8,10]})
#
# ia, ib = np.where(np.less.outer(df_a.a, df_b.c))

# Timestamp = pd.Timestamp
# df1 = pd.DataFrame({'date': (Timestamp('2012-08-01'),
#                              Timestamp('2012-08-02'),
#                              Timestamp('2012-08-03'),
#                              Timestamp('2012-10-29'),
#                              Timestamp('2012-10-30'),
#                              Timestamp('2012-11-01'),
#                              Timestamp('2012-10-15'),
#                              Timestamp('2012-09-04'),
#                              Timestamp('2012-09-05')),
#                     'value': (82, 20, 94, 58, 73, 1, 2, 3, 4)})
# df2 = pd.DataFrame({'end_date':
#                         (Timestamp('2012-10-15'),
#                          Timestamp('2012-09-04'),
#                          Timestamp('2012-11-01')),
#                    'other_value': ('foo', 'bar', 'foobar'),
#                    'start_date': (
#                        Timestamp('2012-09-05'),
#                        Timestamp('2012-08-01'),
#                        Timestamp('2012-10-16'))})
#
# df2 = df2.reindex(columns=['start_date', 'end_date', 'other_value'])
# df2.sort(['start_date'], inplace=True)
#
# date_idx = pd.DatetimeIndex(df1['date'])
# start_date_idx = pd.DatetimeIndex(df2['start_date'])
# end_date_idx = pd.DatetimeIndex(df2['end_date']) + pd.DateOffset(days=1)
#
# start_idx = start_date_idx.searchsorted(date_idx, side='right')-1
# end_idx = end_date_idx.searchsorted(date_idx, side='right')
# df1['idx'] = np.where(start_idx == end_idx, end_idx, np.NaN)
#
# result = pd.merge(df1, df2, left_on = ['idx'], right_index=True)
# result = result.reindex(columns = ['idx', 'data', 'value', 'other_value'])
#
# print(df1)
# print(df2)
# print(result)

# import pandas as pd
# data = pd.read_csv("table.csv", names=["Generator ID", "Month", "Cost"])
#
# data = data.set_index(["Month", "Generator ID"])
# data = data.unstack("Month")
# data.to_csv("HWIN-Costs.csv")

# n = int(input())
# mydict = {}
# for line in range(n):
#     info = input().split(" ")
#     score = map(float, info[1:])
#     mydict[info[0]] = sum(score) / float(len(score))
#
# print("%.2f" % round(mydict[input()],2))


# a = list(map(int, '2 4 5 9'.strip().split(" ")))
# b = list(map(int, '2 4 11 12'.strip().split(" ")))
#
# a2 = [item for item in a if item not in b]
# b2 = [item for item in b if item not in a]
# c2 = a2 + b2
# c2 = set(c2)
#
# print(sorted(c2))



# box = [['Shadab', 8], ['Varun', 8.9], ['Sarvesh', 9.5], ['Harsh', 10]]
#
# box.sort(key=lambda x: x[1])
#
# scores = []
# for i,v in box:
#     scores.append(v)
#
# scores = sorted(set(scores))
# second = scores[1]
#
# for i,v in sorted(box):
#     if v == scores[1]:
#         print(i)


import pandas as pd
import numpy as np
#
# df_a = pd.DataFrame({'a': [1, 2, 3, 4, 1],
#                      'b': [4, 5, 6, 8, 7]})
# df_b = pd.DataFrame({'c': [2, 3, 2],
#                      'd': [7, 8, 10]})
# #
# ia, ib = np.where(np.less.outer(df_a.a, df_b.c))
# # print(pd.concat((df_a.take(ia).reset_index(drop=True),
# #                  df_b.take(ib).reset_index(drop=True)), axis=1))
#
# na = np.setdiff1d(np.arange(len(df_a)), ia)
# nb = -1*np.ones_like(na)
# oa = np.concatenate((ia, na))
# ob = np.concatenate((ib, nb))
# print(pd.concat([df_a.take(oa).reset_index(drop=True),
#                  df_b.take(ob).reset_index(drop=True)], axis=1))


# blah = ['apples', 'oranges', 'apples', 'oranges', 'cherries', 'bananas',
#         'oranges', 'oranges', 'apples', 'nectarine', 'apples', 'nectarine',
#         'bananas', 'bananas', 'oranges', 'cherries', 'cherries', 'nectarine']
# counts = {}
#
# for x in blah:
#     if x in counts:
#         counts[x] += 1
#     else:
#         counts[x] = 1
#
# print(counts)

# data = np.zeros((6,6))
# print(data.ndim)
# print(data.shape)
# print(data.dtype)


# arr = np.arange(32).reshape((8,4))
# print(arr)
# print(arr[[1,5,7,2], [0, 3, 1, 2]])


# x = np.random.randn(8)
# y = np.random.randn(8)
# print(np.maximum(x, y))

# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
#
# z = np.sqrt(xs**2 + ys**2)
# import matplotlib.pyplot as plt
# plt.title("Image Plot of $\sqrt{x^2 + y^2}$ for grid values")
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.show()
#
# large_arr = np.random.randn(1000)
# large_arr.sort()
# print(large_arr[int(0.05*len(large_arr))])


# nsteps = 5000
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws>0, 1, -1)
# walk = steps.cumsum()

# print((np.abs(walk)>=10).argmax())


# import matplotlib.pyplot as plt
# plt.plot(walk)
# plt.show()

# data = pd.DataFrame(np.arange(16).reshape(4,4))
# print(data)
#
# def f(x):
#     return pd.Series([x.max(), x.min()], index=['min', 'max'])
#
# print(data.apply(f))
#
# g = lambda x: x.max() - x.min()
# print(data.apply(g, axis=1))

# df = pd.DataFrame(np.random.randn(3, 3))
# print(df.applymap(lambda x: '%.2f' %x))

# import pandas.io.data as web
# all_data = {}
#
# for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
#     all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
#
# price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
# volume = pd.DataFrame({tic: data['Volume'] for tic, data in all_data.items()})
# print(all_data.items())

# import pandas.io.data as web
# import datetime
#
# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2013, 1, 27)
#
# f = web.DataReader("F", 'yahoo', start, end)
# g = f.ix['2010-01-04']
# print(g)

# arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
#           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
#
# tuples = list(zip(*arrays))
#
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# s = pd.Series(np.random.randn(8), index=index)
# print(s)

# iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
# index = pd.MultiIndex.from_product(iterables, names=['first', 'second'])

# s = pd.Series(np.random.randn(8), index=index)
# print(s)

# df = pd.DataFrame(np.random.randn(4,8), columns=index, index=list('ABCD'))
# print(df)
# print('----'*8)
# print(df['bar', 'one'])


# print(s)
# print('----'*10)
# print(s[:-2])
# print('----'*10)
# print(s+s[:-2])
# print('----'*10)
# print(s[::2])
# print(s+ s[::2])

# df = df.T
# print(df.loc['bar'])

# def mklbl(prefix, n):
#     return ["%s%s" % (prefix, i) for i in range(n)]
#
# miindex = pd.MultiIndex.from_product([ mklbl('A', 4),
#                                        mklbl('B', 2),
#                                        mklbl('C', 4),
#                                        mklbl('D', 2)])
#
# micolumns = pd.MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'),
#                                        ('b', 'foo'), ('b', 'blah')],
#                                       names=['lv10', 'lv11'])
#
# dfmi = pd.DataFrame(np.arange(len(miindex)*len(micolumns)).reshape((len(miindex), len(micolumns))),
#                     index=miindex, columns = micolumns).sort_index().sort_index(axis=1)
# print(dfmi)


# first = ['bar', 'baz', 'foo', 'qux']
# second = ['one', 'two']
#
# from itertools import product
# c = list(itertools.product(first, second))

# multiindex = pd.MultiIndex.from_tuples(c, names=['first', 'second'])
#
# df = pd.DataFrame(np.abs(np.random.randn(8,3)), columns=['A', 'B', 'C'], index=multiindex)
# df = df.T
# # print(df.loc[:, (slice(None), 'two')])
# # print(df.xs(('foo', 'two'), level=('first', 'second'),axis=1))
# print(df.xs('one', level='second', axis=1))

# first = ['zero', 'one']
# second = ['x', 'y']
# from itertools import product
# c = list(product(first, second))
#
# mii = pd.MultiIndex.from_tuples(c, names=['first', 'second'])
# df = pd.DataFrame(np.abs(np.random.randn(4,2,)), index=mii)
# print(df)
# print(df.sum(level=0))

# import pandas.io.data as web
# pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012')) for stk in
#                       ['AAPL', 'GOOG', 'MSFT', 'DELL']))
# pdata = pdata.swapaxes('items', 'minor')
# # print(pdata['Adj Close'])
# # print(pdata.ix[:, '6/1/2012', :])
# # print(pdata.ix['Adj Close', '5/22/2012':, :])
# stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
# print(stacked)

# def f(a):
#     return np.abs(a)
#
# sentinels = {'a': ['foo'], 'f': ['two']}
# df = pd.read_csv('data.csv', names=['a', 'b', 'c', 'd', 'e', 'f'], na_values=sentinels, converters={'a': f})
#
#
# chunker = pd.read_csv('data.csv', chunksize=1000)
# tot = pd.Series([])
# for piece in chunker:
#     tot = tot.add(piece['key'].value_counts(), fill_value=0)
#

# import csv
# f = open('pydata-book-master'+'/ch06'+'/ex7.csv')
# reader = csv.reader(f)
# contain = []
# for line in reader:
#     contain.append(line)
#
# print(pd.DataFrame(contain))

# import csv
# lines = list(csv.reader(open('pydata-book-master'+'/ch06'+'/ex7.csv')))
# print(pd.DataFrame(lines))

import csv
# lines = [line for line in csv.reader(open('pydata-book-master'+'/ch06'+'/ex7.csv'))]

# lines = list(csv.reader(open('pydata-book-master'+'/ch06'+'/ex7.csv')))
# header, values = lines[0], lines[1]
#
# data_dict = {h:v for h,v in zip(header, zip(*values))}
# print(data_dict)

# with open('pydata-book-master'+'/ch06'+'/ex7.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open('pydata-book-master'+'/ch06'+'/ex7.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)

# with open('pydata-book-master'+'/ch06'+'/ex7.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# lines = [line for line in csv.reader(open('pydata-book-master'+'/ch06'+'/ex7.csv'))]
# header = lines[0]
# values = lines[1:]
#
#
#
# lines_dict = {h:v for h,v in zip(header,zip(*values))}
# print(lines_dict)
#
# a = {}
# for k,v in sorted(lines_dict.items()):
#     print(k, lines_dict[k])

# for key in sorted(lines_dict):
#     print("%s: %s" % (key, lines_dict[key]))

# from lxml.html import parse
# from urllib.request import urlopen
# parsed = parse(urlopen('https://finance.yahoo.com/q/cf?s=YHOO+Cash+Flow'))
# doc = parsed.getroot()
#
# tables = doc.findall('.//table')
# calls = tables[1]
# puts = tables[2]
#
# rows = calls.findall('.//tr')
#
# def _unpack(row, kind='td'):
#     elts = row.findall('.//%s' % kind)
#     return [val.text_content() for val in elts]
#
# from pandas.io.parsers import TextParser
# def parse_options_data(table):
#     rows = table.findall('.//tr')
#     header = _unpack(rows[0], kind='th')
#     data = [_unpack(r) for r in rows[1:]]
#     return TextParser(data, names=header).get_chunk()

# from lxml import objectify
# from io import StringIO
# tag = '<a href="....">Google</a>'
# root = objectify.parse(StringIO(tag)).getroot()
# print(root.text)


# import pymongo
# import requests, json
# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
#
# access_token = "427040407-livDtlMiN8UoNIbLje2JgHkE3HYEv8nr3QLVwKKL"
# access_token_secret = "uvPKSQrnm2neXnf85dNhgK7U4FALp3lI90YuiFKx5dnch"
# consumer_key = "YazCs1RAZt1DTVmUjI62LHIza"
# consumer_secret = "j4Qk4G0VSd08J982mC7IT90QdRI6l4jNWeZSVkFF122OWsiyLc"
#
# class StdOutListener(StreamListener):
#
#     def on_data(self, data):
#         print(data)
#         return(True)
#
#     def on_error(self, status):
#         print(status)
#
# if __name__ == '__main__':
#     # This handles Twitter authentification and the connection to Twitter Streaming API
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)
#
#     # This line filter Twitter Streams to capture data by the keywords
#     stream.filter(track=['python', 'javascript', 'ruby'])


# con = pymongo.MongoClient('localhost', port=27017)
# tweets = con.db.tweets
#
#
# url = 'http://search.twitter.com/search.json?q=python%20pandas'
# data = json.loads(requests.get(url).text)
#
# print(data)

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

# tweets_data_path = '../Test/twitter_data.txt'
#
# tweets_data = []
# tweets_file = open(tweets_data_path, "r")
# for line in tweets_file:
#     try:
#         tweet = json.loads(line)
#         tweets_data.append(tweet)
#     except:
#         continue
#
# tweets = pd.DataFrame()
# tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
# tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
# tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if
#                              tweet['place'] != None else None, tweets_data))
#
#
# def word_in_text(word, text):
#     word = word.lower()
#     text = text.lower()
#     match = re.search(word, text)
#     if match:
#         return True
#     else:
#         return False
#
# tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
# tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
# tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))
#
#
# tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
# tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
# tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or
#                                           word_in_text('tutorial', tweet))
#
# tweets_by_prg_lang = [tweets[tweets['relevant']==True]['python'].value_counts()[True],
#                       tweets[tweets['relevant']==True]['javascript'].value_counts()[True],
#                       tweets[tweets['relevant']==True]['ruby'].value_counts()[True]]
#
#
# prg_langs = ['python', 'javascript', 'ruby']
# x_pos = list(range(len(prg_langs)))
# width = 0.8
# fig, ax = plt.subplots()
# plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
# ax.set_ylabel('Number of tweets', fontsize=15)
# ax.set_title('Ranking": python vs. javascript vs. ruby', fontsize=10, fontweight='bold')
# ax.set_xticks([p + 0.4*width for p in x_pos])
# ax.set_xticklabels(prg_langs)
# plt.grid()
# plt.show()


# prg_langs = ['python', 'javascript', 'ruby']
# tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True],
#                       tweets['ruby'].value_counts()[True]]


# x_pos = list(range(len(prg_langs)))
# width = 0.8
# fig, ax = plt.subplots()
# plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
#
# ax.set_ylabel('Number of tweets', fontsize=15)
# ax.set_title('Ranking: python vs. javascript vs. ruby', fontsize=10, fontweight='bold')
# ax.set_xticks([p+0.4*width for p in x_pos])
# ax.set_xticklabels(prg_langs)
# plt.grid()
# plt.show()


# tweets_by_lang = tweets['lang'].value_counts()
#
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Languages', fontsize=15)
# ax.set_ylabel('Number of tweets', fontsize=15)
# ax.set_title('Top 5 Languages', fontsize=15, fontweight='bold')
# tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
# plt.show()

# tweets_by_country = tweets['country'].value_counts()
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Countries', fontsize=15)
# ax.set_ylabel('Number of tweets', fontsize=15)
# ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
# tweets_by_country[:5].plot(ax=ax, kind='barh', color='red')
# plt.show()


# df1 = pd.DataFrame({'color': ['blue', 'red', 'red', 'blue', 'green', 'red', 'green', 'blue'],
#                     'fruit': ['apple', 'orange', 'banana', 'orange', 'apple', 'apple', 'orange', 'pear'],
#                     'car': ['honda', 'volkswagen', 'mitsubishi', 'tesla', 'chrystler', 'honda', 'tesla', 'tesla']},
#                    index=['Ryan', 'Bob', 'Sherri', 'Elaine', 'Cary', 'Daniel', 'Sally', 'Milly'])
# df2 = pd.DataFrame({'phone number': ['604-452-9288', '604-500-9235', '604-344-8500', '604-520-8389', '604-790-6112',
#                                      '604-434-8493', '604-421-2395', '604-693-3390'],
#                     'city': ['Burnaby', 'Vancouver', 'Vancouver', 'Vancouver', 'Richmond', 'Burnaby', 'Vancouver',
#                              'Surrey']}, index=['Bob', 'Sherri', 'Elaine', 'Greg', 'Sally', 'Mary', 'Fred', 'James'])
# print(df1)
# print('***'*30)
# print(df2)
#
# # df3 = pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
# df3 = df1.join(df2, how='outer')
# print(df3)

# df2.reset_index(inplace=True)
# print(pd.merge(df1, df2, left_index=True, right_on="index", how="outer"))

# df3 = pd.concat([df1, df2], axis=1)
# print(df3)

# from itertools import groupby
# from operator import itemgetter
#
# things = [('2009-09-02', 11),
#           ('2009-09-02', 3),
#           ('2009-09-03', 10),
#           ('2009-09-03', 4),
#           ('2009-09-03', 22),
#           ('2009-09-06', 33)]
#
# for key, items in groupby(things, itemgetter(0)):
#     print(key)
#     for subitem in items:
#         print(subitem)
#     print('-'*20)

# from itertools import chain
# print(list(chain([1,2,3],[4,5,6])))

#
# a=[1,2,3]
# b=[4,5,6]
#
# print(a+b)

# from itertools import tee
# i1, i2, i3 = tee(range(10), 3)
# print(i1)

# from itertools import tee
# r = (x for x in range(10) if x < 6)
# i1, i2, i3 = tee(r, 3)
# print(list(i1))
# print(list(i2))
# print(list(i3))

# from itertools import compress
# print(list(itertools.compress(['a', 'b', 'c'], [True, False, False])))

# s1 = pd.Series([0, 1], index=['a', 'b'])
# s2 = pd.Series([2, 3, 4], index = ['c', 'd', 'e'])
# s3 = pd.Series([5, 6], index=['f', 'g'])
#
# h = pd.concat([s1, s2, s3])
# print(h)
#
# i= pd.concat([s1, s2, s3], axis=1)
# print(i)

# a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=['f', 'e', 'd', 'c', 'b', 'a'])
# b = pd.Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])
#
# b[-1] = np.nan
#
# c = np.where(pd.isnull(a), b, a)
# print(c)

# df = pd.DataFrame({'age': [10, 15, 20, 25, 30, 35, 40, 45, 50],
#                    'gender': ['boy', 'girl', 'boy', 'girl', 'boy', 'girl', 'girl', 'boy',
#                               'boy'],
#                    'pet': ['dog', 'dog', 'dog', 'cat', 'cat', 'dog',
#                            'dog', 'rabbit', 'dog'],
#                    'parents': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no']
#                    }, index=['bob', 'randy', 'ellen', 'ryan', 'sam', 'barry', 'sean', 'sherri', 'kyle'])
#
# df.index.name = 'name'
# df.reset_index(inplace=True)
#
# print(df)
#
# df_pivot = df.pivot(index='name', columns='pet', values='age')
# print(df_pivot)


# df = pd.DataFrame({'sample type': list('AAAABBBBBCCCCC'),
#                    'date': pd.date_range(pd.datetime.today(), periods=len(list('AAAABBBBBCCCCC'))).tolist(),
#                   'value': np.random.randn(len(list('AAAABBBBBCCCCC')))})
#
# df.index.name = "id"
#
# # pivoted = df.pivot('date', 'sample type', 'value')
# # print(pivoted)
#
# df = df.rename(index = str.title, columns = str.upper)
#
# print(df)
# df.index.map(str.lower)


# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
#
# cats = pd.cut(ages, bins)
# print(pd.value_counts(cats))

# df = pd.DataFrame(np.arange(4*5).reshape(5,4))
# sampler= np.random.permutation(5)
# # df = df.take(sampler)
# # print(df)
#
# # df = df.take(np.random.permutation(len(df))[:3])
# # print(df)
#
# bag = np.array([5, 7, -1, 6, 4])
# sampler = np.random.randint(0, len(bag), size=10)
# draws = bag.take(sampler)
# print(draws)

# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
#                    'data1': range(6)})
# df2 = pd.get_dummies(df['key'])
# df3 = pd.get_dummies(df['key'], prefix='key')
# dummies = pd.get_dummies(df['key'], prefix='key')
# df_with_dummy = df[['data1']].join(dummies)
# print(df_with_dummy)

# movies = pd.DataFrame({'movie_id': range(10),
#                    'title': ['Toy Story (1995)', 'Jumanji (1995)', 'Grumpier Old Men (1995)',
#                   'Waiting to Exhale (1995)', 'Father of the Bride II (1995)', 'Heat (1995)', 'Sabrina (1995)',
#                              'Tom and Huck (1995)', 'Sudden Death (1995)', 'GoldenEye (1995)'],
#                    'genres': ['Animation|Children\'s|Comedy', 'Adventure|Children\'s|Fantasy',
#                               'Comedy|Romance', 'Comedy|Drama', 'Comedy', 'Action|Crime|Thriller', 'Comedy|Romance',
#                               'Adventure|Children\'s', 'Action', 'Action|Adventure|Thriller']})
#
# genre_iter = (set(x.split('|')) for x in movies.genres)
# genres = sorted(set.union(*genre_iter))
#
# dummies = pd.DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
#
# for i,gen in enumerate(movies.genres):
#     dummies.ix[i, gen.split('|')] = 1
#
# movies_windic = movies.join(dummies.add_prefix('Genre_'))
# print(movies_windic.ix[0])


# import re
# # text = "foo    bar\t baz   \tqux"
# # # print([c.strip() for c in text.split()])
# # f = re.split('\s+', text)
# # regex = re.compile('\s+')
# #
# # print(regex.findall(text))
#
# text = """Dave dave@google.com
# Steve steve@gmail.com
# Rob rob@gmail.com
# Ryan ryan@yahoo.com
# """
#
# # pattern = r'\w*@\w*\.[A-Z]{2,4}'
# # regex = re.compile(pattern, flags=re.IGNORECASE)
# # regex.findall(text)
# # m = regex.search(text)
# # text[m.start(): m.end()]
# # # print(regex.match(text))
# # print(regex.sub('REDACTED', text))
#
# pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
# regex = re.compile(pattern, flags=re.IGNORECASE)
# m = regex.findall(text)
# print(m)

# df = pd.DataFrame({'name': ['Riley', 'Bob', 'Sean', 'Greg', 'Larry'],
#                    'age': [26, 30, 38, 16, 23],
#                    'email': ['rileyhun@hotmail.com', 'bobswartz@ibm.net', 'seanlewis@yahoo.ca', 'gregswarry@hotmail.com',
#                              'larryswells@gmail.com']})
# # print(df[df['email'].str.contains('hotmail.com')])
# pattern = r'\w+@\w+\.[a-z]{2,4}'
# # print(df['email'].str.findall(pattern, flags=re.IGNORECASE))
# df['email']=df['email'].str.replace(pattern, 'hi')
# print(df)
#


# import json
# import matplotlib.pyplot as plt
# db = json.load(open("pydata-book-master/ch07/foods-2011-10-03.json"))
# info_keys = ['description', 'group', 'id', 'manufacturer']
# info = pd.DataFrame(db, columns=info_keys)
#
#
# nutrients = []
# for rec in db:
#     fnuts = pd.DataFrame(rec['nutrients'])
#     fnuts['id'] = rec['id']
#     nutrients.append(fnuts)
#
# nutrients = pd.concat(nutrients, ignore_index=True)
# nutrients = nutrients.drop_duplicates()
# col_mapping = {'description': 'food', 'group': 'fgroup'}
# info = info.rename(columns=col_mapping, copy=False)
# col_mapping = {'description': 'nutrients', 'group': 'nutgroup'}
# nutrients = nutrients.rename(columns=col_mapping, copy=False)
#
#
# ndata = pd.merge(nutrients, info, on='id', how='outer')
# result = ndata.groupby(['nutrients', 'fgroup'])['value'].quantile(0.5)
# result['Zinc, Zn'].order().plot(kind='barh')
# # plt.show()
#
# by_nutrient = ndata.groupby(['nutgroup', 'nutrients'])
# get_maximum = lambda x: x.ix[x.value.idxmax()]
# get_minimum = lambda x: x.ix[x.value.idxmin()]
#
# max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]
# print(max_foods.ix['Amino Acids']['food'])
#
#
# for n in range(2,10):
#     for x in range(2, n):
#         if n%x == 0:
#             print(n, 'equals', x,"*", n//x)
#             break
#     else: print(n, 'is a prime number')


# def is_prime(a):
#     return all(a%i for i in range(2,a))
#
# for i in range(1,100):
#     if is_prime(i)==True:
#         print(i, "is a prime number")
#     else: print(i, "is not a prime number")
#
#

# def even_number(a):
#     if a%2==0:
#         return(True)
#     else:
#         return(False)
#
# for i in range(1, 10):
#     print(i,even_number(i))

# def fib2(n):
#     result=[]
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return(result)

# def f(a, L=[]):
#     L.append(a)
#     return L
# print(f(8))
# print(f(10))
# print(f(182))


# def lets_talk(*arguments, **keywords):
#     for arg in arguments:
#         print(arg)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
# arg = [10, 15, 60]
# conversation = {'Ryan': "Hey! How's it going?",
#                 'Bob': "I am so hungry!",
#                 'Tana': "I like to eat!"}
# lets_talk(arg, conversation)

# def test_var_args(farg, *args):
#     print("formal arg:", farg)
#     for arg in args:
#         print("another arg:", arg)
#
# test_var_args(1, "two", 3, 20, 650, 290, 5810)

# def _test_a(*args, **kvargs):
#     if args:
#         _test_function(*args)
#     elif kvargs:
#         _test_function(**kvargs)
#
# def _test_function(stringValue, intValue, floatValue):
#     print('value1: %s, value2: %d, value3: %f' % (stringValue, intValue, floatValue))
#
# dict_params = {'stringValue': 'Nami', 'intValue': 23, 'floatValue': 34.67}
# _test_a(**dict_params)


# def print_everything(*args):
#     for count, thing in enumerate(args):
#         print('{}. {}'.format(count, thing))
#
# print_everything('apple', 'banana', 'cabbage', 'chicken')

# def table_things(**kwargs):
#     for name, value in kwargs.items():
#         print('{} = {}'.format(name, value))
#
# table_things(apple = 'fruit', cabbage='vegetable')

# def testing_args(a, *args, **kwargs):
#     print(a)
#     for i in args:
#         print('It is', i)
#
#     if kwargs is not None:
#         for key, value in sorted(kwargs.items()):
#             print(key, value)
#
# testing_args('apple', 'banana', 'cherry', 12, 13, 15, 'bob', boy = 'Riley', girl = 'Jeanette')
# from functools import reduce
# # foo = [1, 2, 3, 4, 5 , 6, 7]
# # print(reduce(lambda x, y: x+y, foo))
#
# input_list = [[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]]
# result = reduce(set.intersection, map(set, input_list))
# print(result)

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# # pairs = list(zip(*pairs))
#
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# yay = [ele**2 for inside in matrix for ele in inside]
# print(yay)

#
# vec = [-4, 2, 0, 2, 4]
# print(list(filter(lambda x: x < 0, vec)))
# print([ele for ele in vec if ele < 0])

# import math
# print('The value of pi is %.5f' %math.pi)

# class Error(Exception):
#     pass
#
# class InputError(Error):
#     def __init__(self, expression, manage):
#         self.expression = expression
#         self.message = manage
#
# class TransitionError(Error):
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message
#
#
# try:
#     raise InputError(5*5)
# except InputError as e:
#     print("")



# raw_data = [np.nan, 78, 34, 23, np.nan, 23, 18, 1, np.nan]
# print(raw_data)
#
# # filtered_data = []
# # for i in raw_data:
# #     if not np.isnan(i):
# #         filtered_data.append(i)
# #
# # print(filtered_data)
#
# # filtered_data = list(filter(lambda x: np.isfinite(x), raw_data))
# # print(filtered_data)
#

# n = 3
#
# my_dict = {}
# for i in range(n):
#     info = input().split(" ")
#     score = list(map(float, info[1:]))
#     my_dict[info[0]] = sum(score)/float(len(score))


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# # print([ele for sublist in matrix for ele in sublist])
# # matrix = np.array(matrix).T
# # print(matrix)
#
# print(list(zip(*matrix)))
# [[row[i] for row in matrix] for i in range(len(matrix))]

# questions = ['name', 'quest', 'favourite color']
# answers = ['lancelot', 'holy grail', 'blue']
#
# for q,a in zip(questions, answers):
#     print('What is your {0}? It is {1}'.format(q, a))

# my_dict = {'name': 'lancelot',
#            'quest': 'holy grail',
#            'favourite color': 'blue'}
#
# for i in sorted(my_dict.keys()):
#     print('What is your %s? It is %s' % (i, my_dict[i]))
#

# df = pd.DataFrame({'AAA': [4,5,6,7],
#                    'BBB': [10, 20, 30, 40],
#                    'CCC': [100, 50, -30, -60]})

# df_mask = pd.DataFrame({'AAA': [True]*4,
#                         'BBB': [False]*4,
#                         'CCC': [True, False]*2})

# df[~df_mask] = -1000
# print(df)

# mask = df.AAA < 6
# df[mask] = 1000
# print(df)

# df = df.ix[(df.BBB-43).abs().argsort()]
# print(df)

# dates = pd.date_range('1/1/2000', periods=8)
# df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# panel = pd.Panel({'one': df, 'two': df-df.mean(), 'three': df-df.sum()})
#
# mask = (panel['one'] > 0) & (panel['three'] > 0)
# masked_values = np.where(mask, panel.values, np.nan)
#
# x = pd.Panel(masked_values, **panel._construct_axes_dict())
#

# df = pd.DataFrame(
#     {'AAA': [1,2,1,3], 'BBB': [1,1,2,2], 'CCC': [2,1,3,1]})

# source_cols = df.columns
# new_cols = [str(x) + "_cat" for x in source_cols]
# categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
# df[new_cols] = df[source_cols].applymap(categories.get)
# print(df)

# df2 = df.rename(columns={'AAA': 'AAA_cat', 'BBB': 'BBB_cat', 'CCC': 'CCC_cat'})
#
# for i in ['AAA_cat', 'BBB_cat', 'CCC_cat']:
#     df2[i] = np.where(df2[i]==1, "Alpha", np.where(df2[i]==2, "Beta", "Charlie"))
#
# print(df)
# print(df2)
#
# print(pd.merge(df, df2, left_index=True, right_index=True))

# df = pd.DataFrame({'row': [0, 1, 2],
#                    'one_x': [1.1, 1.1, 1.1],
#                    'one_y': [1.2, 1.2, 1.2],
#                    'two_x': [1.11, 1.11, 1.11],
#                    'two_y': [1.22, 1.22, 1.22]})
#
# df = df.set_index('row')
# index = pd.MultiIndex.from_tuples(tuple(c.split('_') for c in df.columns))
# df.columns = index
#
# df = df.stack(0).reset_index(1)
# df.columns = ['sample', 'All_X', 'All-Y']
# df.set_index('sample')
# print(df)


# arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
#           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
#
# import itertools
# tuples = list(zip(*arrays))
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# cols = pd.MultiIndex.from_tuples([('apples', 'AA'), ('apples', 'BB'), ('oranges', 'CC'), ('oranges', 'DD')],
#                                  names=['fruit', 'alpha'])
#
# data = pd.DataFrame(np.random.randn(8,4), columns=cols, index=index)
# # print(data.xs('one', level=1, axis=0))
#
# data = data.reset_index()
# print(data)
# # print(pd.pivot_table(data, index=['first', 'second'], columns=['AA']))

# df = pd.DataFrame({'index' : range(8),
# 'variable1' : ["A","A","B","B","A","B","B","A"],
# 'variable2' : ["a","b","a","b","a","b","a","b"],
# 'variable3' : ["x","x","x","y","y","y","x","y"],
# 'result': [1,0,0,1,1,0,0,1]})
#
# df2 = df.pivot_table(values='result', index='index', columns=['variable1', 'variable2', 'variable3'])
# df2.loc[:,(slice(None), slice(None), 'y')] = df2.loc[:,(slice(None), slice(None), 'y')].fillna(method='ffill')
# print(df2)

# x = df.swaplevel('variable1', 'variable3', axis=1)
# x['y'] = x['y'].ffill()
# x.swaplevel('variable3', 'variable1', axis=1)

# df2 = df2.stack(['variable1', 'variable2'])
# print(df2.unstack(['variable1', 'variable2']))
#
#
# df = pd.DataFrame(np.random.randn(6,1), index=pd.date_range('2013-08-01', periods=6, freq='B'), columns=list('A'))
# df.ix[3, 'A'] = np.nan
# df2 = df.reindex(df.index[::-1]).ffill()
#
# print(df)
# print(df2)

# df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
#                    'size': list('SSMMMLL'),
#                    'weight': [8, 10, 11, 1, 20, 12, 12],
#                    'adult': [False]*5 + [True]*2})
# # list size of animals with highest weight
# # df2 = df.groupby('animal')['weight'].idxmax()
# # print(df.ix[df2].reset_index(drop=True)[['animal', 'size']])
#
# df2 = df.groupby('animal').apply(lambda subf: subf['size'].ix[subf['weight'].idxmax()])

# rand = np.random.RandomState(1)
# df = pd.DataFrame({'A': ['foo', 'bar'] * 3,
#                    'B': rand.randn(6),
#                    'C': rand.randint(0, 20, 6)})
# gb = df.groupby(['A'])
# print(gb.get_group('foo'))

# def GrowUp(x):
#     avg_weight = sum(x[x['size'] == 'S'].weight*1.5)
#     avg_weight += sum(x[x['size'] == 'M'].weight*1.25)
#     avg_weight += sum(x[x['size'] == 'L'].weight)
#     avg_weight /= len(x)
#     return pd.Series(['L', avg_weight, True], index=['size', 'weight', 'adult'])
#
# expected_df = df.groupby('animal').apply(GrowUp)
# print(expected_df)\



# test_dup_df = pd.DataFrame({'group': ['A', 'B', 'A', 'C', 'C', 'B', 'B', 'A', 'C', 'A'],
#                             'exe_price': [84.5, 85.0, 84.5, 84.5, 84.5, 84.5, 84.5, 84.5, 84.5, 84.5],
#                             'exe_vol': [200, 10000, 69700, 1200, 1000, 300, 88100, 11900, 5000, 3200],
#                             'flag': ['yes']*10})
#
# def grouper(x):
#     cost = sum(x[x['group']=='A'].exe_price*x[x['group']=='A'].exe_vol)
#     cost += sum(x[x['group']=='B'].exe_price*x[x['group']=='B'].exe_vol)
#     cost += sum(x[x['group']=='C'].exe_price*x[x['group']=='C'].exe_vol)
#     cost /= len(x)
#     return pd.Series([cost, True], index=['cost', 'flag'])
#
# print(test_dup_df.sort(['group']))
# print(test_dup_df.groupby('group').apply(grouper))
#
# s = pd.Series([i/100 for i in range(1,11)])
# print(s)
#
# def CumRet(x, y):
#     return x*(1+y)
#
# def Red(x):
#     return functools.reduce(CumRet, x, 1.0)
#
# # H = pd.expanding_apply(s, lambda s: functools.reduce(lambda x, y: x*(1+y), s, 1))
# # print(H)
#
# H = pd.expanding_apply(s, Red)
# print(H)

# s = pd.Series([i/100 for i in range(1,11)])
#
# def cool(x):
#     return x.sum()/len(x)
# print(s)
# print(pd.expanding_apply(s, cool))
# print(pd.expanding_mean(s))

# import random
# df = pd.DataFrame({'animal': ['cat', 'dog', 'cat', 'dog', 'bear', 'bear', 'bear', 'dog', 'cat', 'bear', 'cat'],
#                    'value': [random.choice([0,1]) for _ in range(11)],
#                    'value2': np.random.randint(0,2,11),
#                    'color': [random.choice(['blue', 'red', 'green']) for _ in range(11)]}
#                   )
# print(df)
# print('*'*30)
#
# df['value3']= df.groupby('animal')['value'].transform(lambda x: (x - x.mean())/x.std())
# print(df.sort(['animal']))
#
# print('*'*30)
#
# def replace(g):
#     mask = g < 3
#     g.loc[mask] = g[~mask].mean()
#     return g
#
# df['value3'] = df.groupby('animal')['value'].transform(replace)
# print(df.sort(['animal']))

# def special(x):
#     mask = x < 1
#     x.loc[mask] = x.loc[~mask].sum()
#     return x
#
# df['value3'] = df.groupby('animal')['value'].transform(special)
# print(df)

# df = pd.DataFrame({'code': ['foo', 'bar', 'baz'] * 2,
#                     'data': [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],
#                     'flag': [False, True] * 3})
#
# g = df.groupby('code')['data'].apply(lambda x: x.sort_values())
# print(g)

# rand = np.random.RandomState(1)
# df = pd.DataFrame({'A': ['foo', 'bar', 'baz'] * 2,
#                             'B': rand.randn(6),
#                             'C': rand.rand(6) > .5})
#
# # dg = df.groupby('A')['B'].sum()
# #
# # df['order1'] = df.groupby('A')['B'].transform(np.sum)
# # print(df.sort_values(['order1', 'C'], ascending=[True, False]).drop('order1', axis=1))
#
# grp = df.groupby('A')
# g = grp[['B']].transform(sum).sort('B')
# print(g)
# sort1 = df.ix[g.index]
# sort2 = sort1.groupby('A', sort=False).apply(lambda x: x.sort_values('C', ascending=False))
# print(sort2)

# rng = pd.date_range('2014-10-07', periods=10, freq='2min')
# ts = pd.Series(data=list(range(10)), index=rng)
#
# def mycust(x):
#     return x.mean() - x.std()
#
# mhc = {'mean': np.mean, 'max': np.max, 'custom': lambda x: x.std()}
# g = ts.resample('5min', how=mhc)
# print(g)

# df = pd.DataFrame({'Color': 'Red Red Red Blue'.split(),
#                   'Value': [100, 150, 50, 50]})
#
# df['counts'] = df.groupby('Color', as_index=False)['Value'].transform(lambda s: s.count())
# print(df)

# df = pd.DataFrame(
#  {u'line_race': [10, 10, 8, 10, 10, 8],
#  u'beyer': [99, 102, 103, 103, 88, 100]},
#  index=[u'Last Gunfighter', u'Last Gunfighter', u'Last Gunfighter',
#           u'Paynter', u'Paynter', u'Paynter'])
#
# df['beyer_shifted'] = df.groupby(level=0)['beyer'].shift(1)
# print(df)

# select row with maximum value from each group
# df = pd.DataFrame({'host':['other','other','that','this','this'],
#                    'service':['mail','web','mail','mail','web'],
#                 'no':[1, 2, 1, 2, 1]}).set_index(['host', 'service'])
# print(df.ix[df.groupby(level=0)['no'].idxmax()])

#grouping like Python's itertools Groupby

# df = pd.DataFrame([0, 1, 0, 1, 1, 1, 0, 1, 1], columns=['A'])
# print(df)

# from itertools import groupby
#
# things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
#
# for key, group in groupby(things, lambda x: x[0]):
#     for thing in group:
#         print("A %s is a %s." % (thing[1], key))
#     print("")

# import itertools
#
# listofnumbers = 'alessandraisthegreatest'
# freq = [(c, len(list(gen))) for c, gen in itertools.groupby(listofnumbers)]
# print(freq)

# from itertools import groupby
# from operator import itemgetter
#
# for key, items in groupby(things, lambda x: x[0]):
#     print(key)
#     for subitem in items:
#         print(subitem[0] + ", " + subitem[1])
#     print('-'*30)


# test_scores = [('Math', 80), ('Math', 85), ('English', 90), ('History', 76), ('English', 99), ('English', 99),
#                ('Math', 54), ('Math', 50), ('English', 88), ('English', 66), ('History', 87), ('History', 70),
#                ('Math', 45), ('English', 66), ('History', 69), ('Science', 85), ('Science', 70), ('Science', 77),
#                ('History', 87), ('English', 74), ('Science', 50), ('Science', 56), ('Math', 57), ('English', 59)]
#
# print(test_scores)
# from itertools import groupby
# # from operator import itemgetter
# # for key, items in groupby(sorted(test_scores), itemgetter(0)):
# #     print(key)
# #     for subitem in items:
# #         print(subitem)
# #     print('-'*20)
#
# for key, items in groupby(sorted(test_scores), lambda x: x[0]):
#     print(key)
#     for subitem in items:
#         print(subitem[1])
#     print('-'*30)


# df = pd.DataFrame({'animal': ['bear', 'bunny', 'bear', 'bunny', 'bear','bunny', 'bunny', 'bear', 'bear'],
#                     'value': [0, 1, 0, 1, 1, 1, 0, 1, 1]
# })
# df['cumulative'] = df.groupby('animal')['value'].cumsum()
# print(df)

# df = pd.DataFrame({'Basket': [88, 88, 88, 123, 477, 477, 566],
#                    'Date': ['3-01-2012', '11-02-2012', '16-08-2012', '18-06-2012', '19-08-2012', '11-12-2012',
#                             '6-07-2012'],
#                   'Sale': [15, 30, 16, 90, 77, 57, 70]}, index=None)
# print(df)
#
# from pandas import concat
# from pandas.stats.moments import expanding_mean, expanding_count
#
# def handler(grouped):
#     se = grouped.set_index('Date')['Sale'].sort_index()
#     return concat(
#         {'PrevSale': se.shift(1),
#          'MaxToDate': se.cummax(),
#          'MeanToDate': expanding_mean(se),
#          'Sale': se,
#          'SaleCount': expanding_count(se)},
#         axis=1
#     )
#
# new_df = df.groupby('Basket').apply(handler).reset_index()
# print(new_df)

# df = pd.DataFrame({'RollBasis': [1,1,1,2,3,5,8, 10, 12, 13],
#                    'ToRoll': [1,4,-5,2,-4,-2, 0, -13, -2, -5]})
# print(df)
#
# def f(x):
#     ser = df['ToRoll'][(df['RollBasis']>=x) & (df['RollBasis'] <x+5)]
#     return ser.sum()
#
# df['Rolled'] = df['RollBasis'].apply(f)
# print(df)

# g = df.groupby(pd.cut(df['RollBasis'], bins=[0,5,10,13])).sum()
# print(g)


# df = pd.DataFrame({'enddate': pd.date_range('2016-06-01', freq='6H', periods=30),
#                    'favourable': abs(np.random.normal(0,1,size=30)),
#                    'unfavourable': abs(np.random.normal(0,1,size=30)),
#                    'other': abs(np.random.normal(0,1,size=30))})
# df.set_index('enddate', inplace=True)
# df = df.resample("1D", fill_method="ffill")
# print(df)
# print(pd.rolling_mean(df, window=3, min_periods=1))

# df = pd.DataFrame({'a': ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A'],
#                   'b': np.random.normal(0,1,9)})
# df['grpb'] = np.nan
# df['grpb'][df[df['a']=='B'].index] = range(len(df[df['a']=='B'].index))
# df=df.fillna(method='bfill').fillna(len(df[df['a']=='B'].index))
# print(df)
#
# gg = list(df.groupby((df.a =='B').shift(1).fillna(0).cumsum()))
# print(gg[0])

# grades = [48,99,75,80,42,80,72,68,36,78]
#
# df = pd.DataFrame( {'ID': ["x%d" % r for r in range(10)],
#                'Gender' : ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M'],
#                 'ExamYear': ['2007','2007','2007','2008','2008','2008','2008','2009','2009','2009'],
#              'Class': ['algebra', 'stats', 'bio', 'algebra', 'algebra', 'stats', 'stats', 'algebra', 'bio', 'bio'],
#            'Participated': ['yes','yes','yes','yes','no','yes','yes','yes','yes','yes'],
#               'Passed': ['yes' if x > 50 else 'no' for x in grades],
#                'Employed': [True,True,True,False,False,False,False,True,True,False],
#   'Grade': grades})
#
# df = df.groupby('ExamYear').agg({'Participated': lambda x: x.value_counts()['yes'],
#                               'Passed': lambda x: sum(x=='yes'),
#                               'Employed': lambda x: sum(x),
#                               'Grade': lambda x: np.mean(x)})
#
#
#
# df = pd.DataFrame(data={'A' : [[2,4,8,16],[100,200],[10,20,30]], 'B' : [['a','b','c'],['jj','kk'],['ccc']]},index=['I','II','III'])
# print(df)
# g = pd.concat(dict([ (x[0], x[1].apply(lambda y: pd.Series(y))) for x in df.iterrows() ]))
# print(g)

# import datetime
#
# rng = pd.date_range('1/1/2000', periods=24, freq='7H')
# df = pd.DataFrame({'time': rng,
#                    'data': np.random.randn(len(rng))+2,
#                    'data2': np.random.randn(len(rng))+2})
# df.set_index('time', inplace=True)
# print(df.ix[df.index.indexer_between_time(datetime.time(7), datetime.time(20))])

# import pandas as pd
# index = pd.date_range('2013-1-1',periods=10,freq='15Min')
# data = pd.DataFrame(data=[1,2,3,4,5,6,7,8,9,0], columns=['value'], index=index)
# print(data)
#
# print(data.ix[data.index.indexer_between_time('1:15', '1:45')])

# rng = pd.date_range('20130101 09:00', '20130110 16:00', freq='30min')
# rng = rng.take(rng.indexer_between_time('09:30', '16:00'))
# rng = rng[rng.weekday<5]
# rng = rng.to_series()
# print(rng)

# df = pd.DataFrame({'Date': pd.date_range('14.03.2013', periods=3),
#                    'h1': np.random.randn(3),
#                    'h2': np.random.randn(3),
#                    'h3': np.random.randn(3),
#                    'h4': np.random.randn(3),
#                    'h5': np.random.randn(3),
#                    'h6': np.random.randn(3),
#                    'h7': np.random.randn(3),
#                    'h8': np.random.randn(3),
#                    'h9': np.random.randn(3),
#                    'h10': np.random.randn(3),
#                    'h11': np.random.randn(3),
#                    'h12': np.random.randn(3),
#                    'h13': np.random.randn(3),
#                    'h14': np.random.randn(3),
#                    'h15': np.random.randn(3),
#                    'h16': np.random.randn(3),
#                    'h17': np.random.randn(3),
#                    'h18': np.random.randn(3),
#                    'h19': np.random.randn(3),
#                    'h20': np.random.randn(3),
#                    'h21': np.random.randn(3),
#                    'h22': np.random.randn(3),
#                    'h23': np.random.randn(3),
#                    'h24': np.random.randn(3)})
# print(df)
#
# from datetime import timedelta
# df = pd.melt(df, id_vars=['Date'])
# df.rename(columns={'variable': 'hour'}, inplace=True)
# df['hour'] = df['hour'].str.replace('h', '').map(lambda x: int(x))
# df['Date'] = df.apply(lambda x: pd.to_datetime(x['Date'], dayfirst=True)+timedelta(hours=x['hour']), axis=1)
# print(df)
#
# from bs4 import BeautifulSoup
# import requests
#
# browser = requests.get("http://www.fin.gc.ca/frt-trf/2015/frt-trf-1506-eng.asp#tbl33")
# soup = BeautifulSoup(browser.text)
# # titles = [a.text for a in soup.find_all('title')]
# # links = [a.text for a in soup.find_all('a')]
# # print(links)
#
# table = soup.findAll("table")
# table5 = table[5]
#
# # parsing data table
#
# rows = table5.find_all('tr')
# data = []
#
# index = [h.text for h in table5.find_all('th', attrs={"scope": "row"})]
#
# for row in rows[1:-1]:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append([ele for ele in cols if ele])
#
# df = pd.DataFrame(data)
# date = pd.Series(index, name="date")
# df = df.join(date).set_index('date')
#
# df = df.rename(columns={0: "a", 1: "b", 2: "c"})
# print(df)

# import urllib.parse
# from urllib.request import urlopen
# from xml.etree import ElementTree
# from lxml import etree
# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.w3schools.com/xml/plant_catalog.xml"
#
# root = etree.parse(urlopen(url)).getroot()
#
# Plants = root.findall('PLANT')
#
# contain = []
# for item in Plants:
#     common = item.find('COMMON').text
#     zone = item.find('ZONE').text
#     price = item.find('PRICE').text
#     availability = item.find('AVAILABILITY').text
#     contain.append([common, zone, price, availability])
#
# df = pd.DataFrame(contain)
# df = df.rename(columns={0: 'Plant Name', 1: 'Zone', 2: 'Price', 3: 'Availability'})
# df['Price'] = df['Price'].str.replace("$", "").astype(float)
# print(df[df.Price<5])
#
# Special_Plants = [item for item in root.findall('PLANT') if item.find('ZONE').text == '3']
# for i in Special_Plants:
#     print(i.find('PRICE').text)


# output = [child.find('PLANT').text for child in root]

# breakfast_menu = [child.find('description').text for child in root]


# request_url = requests.get(url)
# tree = ElementTree.parse(request_url.text)
# root = tree.getroot()
# print(root)
# print([child.find('food').text for child in root])

# request = urlopen(url)
# xml = BeautifulSoup(request, 'xml')
# contain = []
# a = xml.find_all('PLANT')
# print(a)

# import numpy as np
# from pandas import HDFStore, DataFrame
# # # create or open hdf5 file and open in append mode
# # hdf = HDFStore('storage.h5')
# #
# # df = DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
# # # put the dataset in the storage
# # hdf.put('d1', df, format='table', data_columns=True)
#
#
# ## data in storage can be manipulated. Can append new data to dataset just created
# # hdf.append('d1', DataFrame(np.random.rand(5,3), columns=['A', 'B', 'C']),
# #            format='table', data_columns=True)
# # hdf.close()
#
# ## access data using name of dataset as key
# # print(hdf['d1'].shape)
# # print(hdf['d1'])
# # hdf.close()
#
# # querying data
# from pandas import read_hdf
# # query to select columns A and B where values of A > 0.5
# # hdf = read_hdf('storage.h5', 'd1', where=['A>.5'], columns=['A', 'B'])
# # print(hdf)
#
# # add more datasets to storage, organize using groups
# hdf = HDFStore('storage.h5')
# hdf.put('tables/t1', DataFrame(np.random.rand(20,5)))
# hdf.put('tables/t2', DataFrame(np.random.rand(10,3)))
# hdf.put('new_tables/t1', DataFrame(np.random.rand(15,2)))
#
# print(hdf)
# # can see hierachy of groups added to storage.

# from pandas import HDFStore, DataFrame
# import numpy as np
#
# hdf = HDFStore("collection.h5")
# # df = DataFrame(np.arange(10).reshape((5,2)), columns=['A', 'B'])
# # df2 = DataFrame(np.random.randn(5,2), columns=['C', 'D'])
# # df3 = DataFrame(np.random.randn(5,2), columns=['E', 'F'])
# # hdf.put('simple/data1', df, format='table', data_columns=True)
# # hdf.put('complex/data1', df2, format='table', data_columns=True)
# # hdf.put('complex/data2', df3, format='table', data_columns=True)
#
# # hdf.append('complex/data1', DataFrame(np.random.randn(5,2), columns=['C', 'D']))
# h= hdf['complex/data1'].reset_index(drop=True).join(pd.Series(np.random.randn(10), name='E'))
# print(h)
# hdf.close()

import datetime
from dateutil import parser
import time
# intervals = np.random.randint(0, 1000, size=100).cumsum()
# df = pd.DataFrame({'time': [datetime.datetime.strptime('Jan 1 2014', '%b %d %Y') + pd.offsets.Milli(i)
#                             for i in intervals],
#                    'value': np.random.randn(len(intervals))})
# print(df)

# df = pd.DataFrame({'time': [parser.parse("20140101") + pd.offsets.Milli(i)
#                             for i in intervals],
#                    'value': np.random.randn(len(intervals))})
# print(df)

# df = pd.DataFrame({'time': [pd.to_datetime('20140101') + pd.offsets.Milli(i)
#                             for i in intervals],
#                    'value': np.random.randn(len(intervals))})
#
#
# new_range = pd.date_range('20140101 00:00:00', '20140101 01:00:00', freq='s') + pd.Index(df['time'])
# df2 = df.set_index('time').reindex(new_range).fillna(method='ffill')
# print(df2)
#
# print('new date range that is that union of df.Time and index range ==>')
# print(new_range)
#
# print('new date range ==>')
# print(pd.date_range('20140101 00:00:00', '20140101 01:00:00', freq='s'))
#
# print('df.Time -->')
# print(pd.Index(df['time']))

# dates = pd.date_range('2000-01-01', periods=30, freq='22D')
# print(dates)
# print(dates.to_period(freq='M').to_timestamp())

# time = pd.date_range('2014-01-01 00:15:00', '2017-01-01 00:15:00', freq='15min')
# df = pd.DataFrame({'time': time,
# 'values': np.abs(np.random.randn(len(time)))})
# df.set_index('time', inplace=True)
#
# grouper = pd.TimeGrouper('2M')
# df['normed'] = df.groupby(grouper).transform(lambda x: x/x.mean())
# print(df)

# time = pd.date_range('2008-07-01', '2010-12-01', freq='D')
# monthly_return = pd.DataFrame({'time': time,
#                                'value': np.abs(np.random.randn(len(time)))})
# monthly_return.set_index('time', inplace=True)
#
# Grouper = pd.TimeGrouper('6M', closed='left')
# print(monthly_return.groupby(Grouper).aggregate(numpy.sum))
# print(monthly_return.groupby(Grouper)['value'].sum())

# import random
# time = pd.date_range('2014-01-01 00:15:00', '2017-01-01 00:15:00', freq='30min')
# monthly_return = pd.DataFrame({'time': time,
#                                'value': np.abs(np.random.randn(len(time))),
#                                'branch': [random.choice(['blue', 'red', 'green']) for _ in range(len(time))],
#                                'quantity': np.random.randint(0, 100, len(time))})
# monthly_return.set_index('time', inplace=True)
# Grouper = pd.TimeGrouper('6M')
# # print(monthly_return.groupby(Grouper)['quantity'].apply(lambda x: x.count()))
# # print(monthly_return)
# # print(monthly_return.groupby(Grouper).apply(lambda x: x.count()))
# print(monthly_return.groupby(Grouper).apply(lambda x: x.groupby('branch').sum()))
#
# print(monthly_return)
# print(monthly_return.resample('6M', how='sum'))

# begin = pd.to_datetime('20130101')
# end = pd.to_datetime('20130220')
# dtrange = pd.date_range(begin, end)
#
# p1 = np.random.rand(len(dtrange))+5
# p2 = np.random.rand(len(dtrange))+10
# df = pd.DataFrame({'p1': p1, 'p2': p2}, index=dtrange)
# # print(df)
#
# # calculate dekad's date
# d = df.index.day - np.clip((df.index.day-1) // 10, 0, 2)*10 -1
# date = df.index.values - np.array(d, dtype='timedelta64[D]')
# # df = df.groupby(date).mean()
# # print(df)
# # print(df.index.day)
# # print(np.clip((df.index.day-1) // 10, 0, 2)*10 -1)
# # print(date)

# import random
# dates = pd.date_range('01-Jan-2014', '11-Jan-2014', freq='1H')[0:-1]
# df = pd.DataFrame({'value1': np.random.rand(len(dates)),
#                    'brand': [random.choice(['blue', 'red', 'green', 'yellow']) for _ in
# range(len(dates))],
# 'value2': np.random.rand(len(dates))}, index=dates)
#
#
# df = df.resample('30min', fill_method='ffill')
# # print(df2[df2.index.dayofweek<5])
#
# # df = df.groupby(lambda d: d.date()).resample('30min', fill_method= 'ffill')
# # print(df)
#
# Grouper = pd.TimeGrouper('5D')
# print(df.groupby(Grouper).apply(lambda x: x.groupby('brand').sum()))

# import random
# dates = pd.date_range('01-Jan-2014', '11-Jan-2014', freq='1min')
# df = pd.DataFrame({'value1': np.random.rand(len(dates)),
#                    'brand': [random.choice(['blue', 'red', 'green', 'yellow']) for _ in
# range(len(dates))],
# 'value2': np.random.rand(len(dates))}, index=dates)
# print(df.resample('1H', how=sum, base=30))

# import random
# from datetime import datetime
# # dates = pd.date_range('01-Jan-2014', '01-Jan-2017', freq='1D')
# dates = pd.Series(np.random.choice([datetime.now(), pd.to_datetime('1/1/2001'), pd.to_datetime('11/15/2001'),
#                           pd.to_datetime('12/1/01'),  pd.to_datetime('5/1/01')], size=100), dtype='datetime64[ns]',
#           name='date')
# df = pd.DataFrame({'value1': np.random.randint(len(dates)),
#                    'brand': [random.choice(['blue', 'red', 'green', 'yellow']) for _ in
# range(len(dates))],
# 'value2': np.random.randint(len(dates))}, index=dates)
# resamp = df.groupby('brand').resample('M', how='sum')
# g = resamp.groupby(level = 'date').apply(lambda x: x/x.sum())
# h = g.sortlevel('date').head()
# # print(g.dropna().reset_index())
# print(g.dropna().reset_index().reindex(columns=['date', 'brand', 'value1', 'value2']))

# rng = pd.date_range('2000-01-01', periods=6, name='date')
# df1 = pd.DataFrame(np.random.randn(6,3), index=rng, columns=['A', 'B', 'C'])
# print(df1)
#
# df2 = df1.copy()
# print(df1.append(df2, ignore_index=True))

# df = pd.DataFrame(data={'Area' : ['A'] * 5 + ['C'] * 2,
#                        'Bins' : [110] * 2 + [160] * 3 + [40] * 2,
#                         'Test_0' : [0, 1, 0, 1, 2, 0, 1],
#                        'Data' : np.random.randn(7)})
#
# df['Test_1'] = df['Test_0'] -1
# print(pd.merge(df, df, left_on=['Bins', 'Area', 'Test_0'], right_on=['Bins', 'Area', 'Test_1'], suffixes=['_L', '_R']))

# df = pd.DataFrame({'a': np.random.rand(50),
#                    'b': ['XXXX', 'YYYY']*25},
#                   index=pd.date_range('2012-01-03', periods=50, freq='12h').map(lambda x: x.date()))
#
# df = df.reindex(columns=['b', 'a']).reset_index()
# df = df.rename(columns={'index': 'date', 'b': 'b', 'a': 'a'})
#
# df2 = pd.DataFrame({'a': np.random.rand(50),
#                    'b': ['XXXX', 'YYYY']*25},
#                   index=pd.date_range('2012-01-03', periods=50, freq='12h').map(lambda x: x.date()))
# df2 = df2.reindex(columns=['b', 'a']).reset_index()
# df2 = df2.rename(columns={'index': 'date', 'b': 'b', 'a': 'a'})
#
# dMerged = pd.merge(df, df2, left_on=['date', 'b'], right_on=['date', 'b'])
# print(dMerged)


# df = pd.DataFrame({'CustNum': [32363, 31316],
#                    'CustomerName': ['McCartney, Paul', 'Lennon, John'],
#                    'ItemQty': [3, 25],
#                    'Item': ['F04', 'F01'],
#                    'Seatblocks': ['2:218:10:4:6', '1:13:36:1,12 1:13:37:1,13'],
#                    'ItemExt': [60, 300]})
# s = df.Seatblocks.str.extract('(?P<a>\d+)[:,](?P<b>\d+)[:,](?P<c>\d+)[:,](?P<d>\d+)[:,](?P<e>\d+)$')
# print(df.join(s))


# s = pd.DataFrame(df.Seatblocks.str.split(' ', 1).tolist())
# print(s)

import re
#
# s = df['Seatblocks'].str.split(' ').apply(pd.Series, 1).stack()
# s.index = s.index.droplevel(-1)
# del df['Seatblocks']
# s.name = 'Seatblocks'
# df = df.join(s.str.replace(',', ':').apply(lambda x: pd.Series(x.split(':'))))
# print(df)


# s = "one two 3.4 5,6 seven.eight nine,ten,1.2,a,5"
# print(re.split('\s|(?<!\d)[,.]|[,.](?!\d)', s))


# df = pd.DataFrame({
#                   'Country': ['00000 United States', '01000 Alabama', '01001 Autauga County, AL',
#                               '01003 Baldwin County, AL', '01005 Barbour County, AL']}
#                   )
#
# df = df.Country.str.extract('(?P<fips>\d{5})((?P<state>[A-Z\s]*$)|(?P<county>.*?), (?P<state_code>[A-Z]{2}$))')
# print(df)


# df = pd.DataFrame(df.Country.str.split(' ', 1).tolist(), columns= ['flips', 'row'])
# print(df)

# s = df.Country.str.split(',').apply(pd.Series, 1).stack()
# s.index = s.index.droplevel(-1)
# s.name = 'Country'
# del df['Country']
# df = df.join(s.apply(lambda x: pd.Series(x))).unstack('Number')
# print(df)


# df_a = pd.DataFrame({'a': np.random.randint(1, 10, size=5),
#                      'b': np.random.randint(1, 10, size=5)})
# df_b = pd.DataFrame({'c': np.random.randint(1, 10, size=6),
#                      'd': np.random.randint(1, 10, size=6)})
#
#
# print('df_a ===>')
# print(df_a)
# print('--'*30)
# print('df_b ===>')
# print(df_b)
#
# ia, ib = np.where(np.less.outer(df_a.a, df_b.c))
# g = pd.concat((df_a.take(ia).reset_index(drop=True), df_b.take(ib).reset_index(drop=True)), axis=1)

# ia, ib = np.where(np.less.outer(df_a.a, df_b.c))
# g = pd.concat((df_a.take(ia).reset_index(drop=True), df_b.take(ib).reset_index(drop=True)), axis=1)
# print('--'*30)
# print(g)


#df_b.c > df_a.a
# intervals = np.random.randint(0, 1000, 25)
# time = [pd.to_datetime('20140101 09:30:00') + pd.offsets.Milli(i) for i in intervals]
# intervals2 = np.random.randint(0, 1000, 25)
# time2 = [pd.to_datetime('20140101 09:30:00') + pd.offsets.Milli(i) for i in intervals2]
# df = pd.DataFrame({'time': time,
#                    'bid': np.random.rand(25)+np.random.randint(0,5),
#                   'ask': np.random.rand(25)+np.random.randint(0,5)}, columns = ['time', 'bid', 'ask'])
# df2 = pd.DataFrame({'time': time2,
#     'price': np.random.rand(25)+np.random.randint(0,5),
#                   'size': np.random.randint(0, 100, 25)}, columns = ['time', 'price', 'size'])
#
# print(df)
# print(df2)
# print(pd.ordered_merge(df, df2, fill_method='ffill'))
# print(df.apply(lambda x: x.asof(df2.index)))

# student_login = pd.DataFrame({'id': []})


# Timestamp = pd.to_datetime
# df1 = pd.DataFrame({'date': (Timestamp('2012-08-01'),
#                              Timestamp('2012-08-02'),
#                              Timestamp('2012-08-03'),
#                              Timestamp('2012-10-29'),
#                              Timestamp('2012-10-30'),
#                              Timestamp('2012-11-01'),
#                              Timestamp('2012-10-15'),  # on then end_date
#                              Timestamp('2012-09-04'),  # outside an interval
#                              Timestamp('2012-09-05'),  # on then start_date
#                              ),
#                     'value': (82, 20, 94, 58, 73, 1, 2, 3, 4)})
# df2 = pd.DataFrame({'end_date': (
#                         Timestamp('2012-10-15'),
#                         Timestamp('2012-09-04'),
#                         Timestamp('2012-11-01')),
#                     'other_value': ("foo", "bar", "foobar"),
#                     'start_date': (
#                         Timestamp('2012-09-05'),
#                         Timestamp('2012-08-01'),
#                         Timestamp('2012-10-16'))}, columns=['start_date', 'end_date', 'other_value'])
#
# date_idx = pd.DatetimeIndex(df1.date)
# start_date_idx = pd.DatetimeIndex(df2.start_date)
# end_date_idx = pd.DatetimeIndex(df2.end_date)+pd.DateOffset(days=1)
#
# start_idx = start_date_idx.searchsorted(date_idx, side='right')-1
# end_idx = end_date_idx.searchsorted(date_idx, side='right')
# df1['idx'] = np.where(start_idx==end_idx, end_idx, np.nan)
# result = pd.merge(df1, df2, left_on=['idx'], right_index=True)
# print(result)

# use searchsorted to find where each date in df1 fits amongst the start_dates, and then use searchsorted a second time
# to find where each date fits amongst the end_dates. When the index from the two calls to searchsorted are equal,
# the date falls inside an interval.

# def get_counts(sequence):
#     counts = {}
#     for x in sequence:
#         if x in counts:
#             counts[x] += 1
#         else:
#             counts[x] = 1
#     return counts
#
# a = get_counts([2,3,4,3,4])
# print(a)

# arr = np.empty((8,4))
#
# for i in range(8):
#     arr[i] = i
# print(arr)


# arr = np.arange(32).reshape((8,4))
#
# print(arr)
#
# print(arr[[1,5,7,2], [0, 3, 1, 2]])
#
# print(arr[[1,5,7,2]][:, [0,3,1,2]])

# arr = np.arange(16).reshape((2,2,4))
# print(arr)
#
# print(arr.transpose((1,0,2)))


# random walk

# nsteps = 1000
# # draws = np.random.randint(0, 2, size=nsteps)
# # steps = np.where(draws>0,1, -1)
# walk = steps.cumsum()
#
# print(draws)
# print(steps)

# obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print('b' in obj2)

# df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
#                     'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
#                     'baz': [1, 2, 3, 4, 5, 6]})
#
# print(df)
#
# s = df.pivot('foo', 'bar', 'baz')
#
# print(s.stack('bar').reset_index())

# contain = []
# for i in range(100):
#     contain.append(str(i))
# print("".join(contain))

import numpy as np
import random

integers = [random.randint(0,100) for  _ in range(100)]
print(integers)

integers_dict = {}
for i in integers:
    if i not in integers_dict:
        integers_dict[i] = 1
    else:
        integers_dict[i] += 1

print(integers_dict)


duplicates = []
for i,v in integers_dict.items():
    if v > 1:
        duplicates.append(i)
print(duplicates)

missing = []
for i in range(0,100):
    if i not in integers:
        missing.append(i)
print(missing)

