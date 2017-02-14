import random
def main():
	ranNum = random.randint(1,10)
	print("I thought of a number between 1 and 10.")
	g1 = input("what is your guess? ")
	while(g1 != ranNum):
		if(g1 < ranNum):
			print("Your guess was too low.")
		else:
			print("Your guess was too high.")
		keep_playing = raw_input("Do you want to keep guessing?(y/n) ")
		if(keep_playing == "y"):
			g1 = input("what is your next guess? ")
		else:
			break;

main()
