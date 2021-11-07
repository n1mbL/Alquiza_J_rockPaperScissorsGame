# the compareChosenHands function

def compareChosenHands(status):
	print("called win or lose! You, " + status + "!")
	print("gg")
	print("")
	print("Would you like to play again?")


	if gameVars.player == "scissors":
	if computer == "paper":
		print ("player wins!")
		gameVars.computerLives = gameVars.computerLives -1
	elif computer == "lizard":
		print ("player wins!")
		gameVars.computerLives = gameVars.computerLives -1		
	elif computer == "rock":
		print ("player loses!")
		gameVars.playerLives = gameVars.playerLives -1		
	elif computer == "Spock":
		print ("player loses!")
		gameVars.playerLives = gameVars.playerLives -1		
	else:
		print ("It's a tie!")


	if gameVars.player == "paper":
		if computer == "rock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "Spock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "lizard":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif computer == "scissors":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "rock":
		if computer == "lizard":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "scissors":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "Spock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif computer == "paper":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "lizard":
		if computer == "Spock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "paper":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "scissors":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif computer == "rock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "Spock":
		if computer == "scissors":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "rock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif computer == "paper":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif computer == "lizard":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")

	if gameVars.player == "heal":
		gameVars.playerLives = gameVars.playerLives + 1
		print("Player got healed! ")

	print("computer lives: " + str(gameVars.computerLives))
	print("player lives: " + str(gameVars.playerLives))
	print("")