from gameComponents import gameVars

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
		gameVars.playerLives = 3
		gameVars.computerLives = 3
		gameVars.player = False
		print("computer lives: " + str(gameVars.computerLives))
		print("player lives: " + str(gameVars.playerLives))
		print("Ready to play")