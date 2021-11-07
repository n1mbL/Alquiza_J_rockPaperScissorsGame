# the winOrLose function

def winOrLose(status):
	if status = lost:
		print("You, " + status + "!")
		print("gg")
		print("")
		print("Would you like to play again?")
		choice = input(" Y / N? ")

	if choice == "n":
		print("better luck next time!")
		exit()
	elif choice == "y":
		print("lives reset!")
		gameVars.playerLives = 5
		gameVars.computerLives = 5
		gameVars.player = False
		print("computer lives: " + str(computerLives))
		print("player lives: " + str(playerLives))
		print("")
		