from random import randint
from gameComponents import winOrLose, gameVars, compareChosenHands


# array is just a container, an egg tray. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notation.
choices = ["rock", "paper", "scissors", "lizard", "Spock", "heal"]


# defining a win/lose function and invoke it
# in our game loop when lives run out (player or computer)


# create an infinite loop (for now) so we can keep playing
while gameVars.player is False:

	# save the player as a variable called player
	# the value of player will be one of the five choices to type (input)
	
	gameVars.player = input("Choose rock, paper, scissors, lizard, Spock: ")
	computer = choices[randint(0,4)]

	print("player chose: " + gameVars.player)
	print("computer chose: " + computer)

	if gameVars.playerLives == 0:
		# call the winOrLose function here
		winOrLose.winOrLose("lost")

	elif gameVars.computerLives ==0:
		winOrLose.winOrLose("won")


	# this line below deletes the choice the player made in the previous round
	gameVars.player = False



	#for looping!



	# added a secret heal function that can add 1 new life to the player! :D
