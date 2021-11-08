from gameComponents import winOrLose, gameVars
import main


def compareChosenHands():
#	gameVars.player = input("Choose rock, paper, scissors, lizard, Spock: ")
#	computer = choices[randint(0,4)]

	if gameVars.player == "scissors":
		if main.computer == "paper":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1
		elif main.computer == "lizard":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "rock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif main.computer == "Spock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "paper":
		if main.computer == "rock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "Spock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "lizard":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif main.computer == "scissors":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "rock":
		if main.computer == "lizard":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "scissors":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "Spock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif main.computer == "paper":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "lizard":
		if main.computer == "Spock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "paper":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "scissors":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif main.computer == "rock":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")


	if gameVars.player == "Spock":
		if main.computer == "scissors":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "rock":
			print ("player wins!")
			gameVars.computerLives = gameVars.computerLives -1		
		elif main.computer == "paper":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		elif main.computer == "lizard":
			print ("player loses!")
			gameVars.playerLives = gameVars.playerLives -1		
		else:
			print ("It's a tie!")

	if gameVars.player == "heal":
		gameVars.playerLives = gameVars.playerLives + 1
		print("Player got healed! ")


	# Nov.09 - was showing extra lines of the lives
	print("computer lives: " + str(gameVars.computerLives))
	print("player lives: " + str(gameVars.playerLives))
	print("")

	if gameVars.playerLives == 0:
		# call the winOrLose function here
		winOrLose.winOrLose("lost")


	elif gameVars.computerLives ==0:
		winOrLose.winOrLose("won")

	# this line below deletes the choice the player made in the previous round
	gameVars.player = False