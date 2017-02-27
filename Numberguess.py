import random
def main():
    gigity = random.randint(1, 10)
    print("This is a game where you have to guess a number from 1-10")
    gooo = int(input("What is your first guess (number 1-10 ) "))
    #dog = input("Enter your second guess (1-10) ")


    if (gigity == gooo):
        print("That was right!!!!!!!!!!!!!!!!!!!")
        print("The number was " + str(gigity) + " and you guessed " + str(gooo))


    elif (gigity != gooo):
        print("That was wrong!!!!!!!!!!!!!!!!!!!")
        if (gooo > gigity):
            print("Your guess was too high, guess again ")
            dog = input("Enter your second guess (1-10) ")
            if (gigity == gooo):
                print("That was right!!!!!!!!!!!!!!!!!!!")
                print("The number was " + str(gigity) + " and you guessed " + str(gooo))


            elif (gigity != gooo):
                print("That was wrong!!!!!!!!!!!!!!!!!!!")
                if (gooo > gigity):
                    print("Your guess was too high, now play again ")


                else:
                    print("Your answer was too low, now play again ")

        else:
            print("Your answer was too low, guess again")
            dog = input("Enter your second guess (1-10) ")
            if (gigity == gooo):
                print("That was right!!!!!!!!!!!!!!!!!!!")
                print("The number was " + str(gigity) + " and you guessed " + str(gooo))


            elif (gigity != gooo):
                print("That was wrong!!!!!!!!!!!!!!!!!!!")
                if (gooo > gigity):
                    print("Your guess was too high, now play again ")


                else:
                    print("Your answer was too low, now play again ")


main()