from random import randint
from gameComponents import winOrLose, gameVars


# array is just a container, an egg tray. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notation.
choices = ["rock", "paper", "scissors", "lizard", "Spock", "heal"]


print("")
print("player lives: " + str(gameVars.computerLives))
print("computer lives: " + str(gameVars.playerLives))
print("'There can only be one.' - The Kurgan")
print("")	




# create an infinite loop (for now) so we can keep playing
while gameVars.player is False:

	# the value of player will be one of the five choices to type (input)
	

	gameVars.player = input("Choose rock, paper, scissors, lizard, Spock: ")
	computer = choices[randint(0,4)]

	print("player chose: " + gameVars.player)
	print("computer chose: " + computer)

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

	if gameVars.playerLives == 0:
		# call the winOrLose function here
		winOrLose.winOrLose("lost")


	elif gameVars.computerLives ==0:
		winOrLose.winOrLose("won")

	# this line below deletes the choice the player made in the previous round
	gameVars.player = False




