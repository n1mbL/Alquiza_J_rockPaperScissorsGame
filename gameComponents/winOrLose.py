# the winOrLose function

def winOrLose(status):
	if status == "lost":	
		print("You, " + status + "!")
		print("gg")
		print("")

	elif status == "won":
		print("Computer calls 'gg'")
		print("Congrats! You, " + status + "!")		
		print("")

	print("Would you like to play again?")
	choice = input(" Y / N? ")

	if choice == "n":
		print("better luck next time!")
		exit()
	elif choice == "y":
		print("lives reset!")
		playerLives = 5
		computerLives = 5
		player = False
		print("computer lives: " + str(computerLives))
		print("player lives: " + str(playerLives))
		print("")