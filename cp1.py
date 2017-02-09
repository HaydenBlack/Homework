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
    print(add10(1))


main()
