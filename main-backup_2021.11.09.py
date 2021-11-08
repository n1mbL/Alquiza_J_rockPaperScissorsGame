from random import randint
from gameComponents import winOrLose, gameVars, compareChosenHands


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
	gameVars.player = input("Choose rock, paper, scissors, lizard, Spock: ")
	computer = choices[randint(0,4)]

	compareChosenHands()

#	print("player chose: " + gameVars.player)
#	print("computer chose: " + computer)