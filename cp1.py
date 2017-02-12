# Practice Problems from coding bat
# They should each be their own function inside of this file
# I will show you how to make a function similar to what you will need to be doing
#I can make the new homework from the last lesson here

blah = True

def near_hundred(n):
    if (n > 89 and n < 111):
        return True
    else:
        return False

def makes10(a, b):
    if (a == 10 or b == 10):
        return True
    elif (a + b == 10):
        return True
    else:
        return False

def monkey_trouble(x, z):
    if (x == True and z == True):
        print("Your in trouble")
        return True
    elif (x == False and z == True):
        print("You are safe")
        return False
    elif (x == True and z == False):
        print("You are not in trouble")
        return False
    else:
        print("You are in trouble")
        return True

def add10(x):
    if (x < 100):
        y = x + 10
        #print(y)
        return add10(y)
    else:
        #print(x)
        return(x)

<<<<<<< HEAD
def make_abba(a, b):
    che = input("Enter a word ")
    we = input("Enter another word ")
    print(che + we + we + che)
    return (a, b)
=======
"""
Given a string name("Bob"),
return a greeting in the form "Hello Bob!".
Example:
hello_name('Bob'), prints 'Hello Bob!'
hello_name('Alice'), prints 'Hello Alice!'

Make the changes to the function below
then add it to the main function below to tell it to run hello_name
hint: it runs similar to how the other functions in main are running
"""
def hello_name(name):



"""
Given two strings, a and b, return the result of putting them together in the order abba,
Example:
"Hi" and "Bye" returns "HiByeByeHi"
make_abba('Hi', 'Bye') returns 'HiByeByeHi'
make_abba('Yo','Scott') returns 'YoScottScottYo'
make_abba('What', 'Up') returns 'WhatUpUpWhat'

Hint: Think about how you attach a variable to a print statement
print("words"... "more words"), it is called concatenation,
or concatenating strings if you need to look it up.
"""
def make_abba(a, b):


>>>>>>> 89b34f3d76bd49af4cc986ccd425890047887c1e


def main():

    x = True

    print("Hello")
    near_hundred(99)
    near_hundred(1000)
    makes10(7, 9)
    makes10(1, 10)
    makes10(9, 1)
    monkey_trouble(x, False)
    monkey_trouble(blah, blah)
    (add10(1))
    print(make_abba(1, 2))



main()
