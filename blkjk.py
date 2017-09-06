import random

def newDraw():
	num = random.randrange(1,11)
	return num

def main():
	print("----------This is a blackjack game. Good luck!----------")
	dealersFirst = 10
	dealersSecond = random.randrange(1,11)
	dealersHand = dealersFirst + dealersSecond
	print(dealersSecond, dealersHand)

	playFirst = newDraw()
	testPrompt = ""

	while(testPrompt != "n"):
		testPrompt = input("You have " + str(playFirst) + ".\nContinue to hit or stay (y/n)? ")
		if (testPrompt == "y"):
			playFirst = playFirst + newDraw()
		else:
			if(playFirst == 21):
				print("You got blackjack! You have received credit.")
			if (playFirst > 21):
				print("Game over. You lose!")
			elif (playFirst > dealersHand):
				print("Winner! You have recieved credit.")
			else:
				print("You are a loser. Try the game again.")


main()