from random import randint

# add player and computer lives
playerLives = 5
computerLives = 5

# if (playerLives = 0)
#	print ("Computer beat you!")
#else:
#	print ("You beat the computer!")

# save the player as a variable called player
# the value of player will be one of the five choices to type (input)

player = input("Choose rock, paper, scissors, lizard, Spock: ")

print("player chose: " + player)

# array is just a container, an egg tray. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notation.
choices = ["rock", "paper", "scissors", "lizard", "Spock", "heal"]

computer = choices[randint(0,4)]

print("computer chose: " + computer)

if (player == "scissors"):
	if (computer == "paper"):
		print ("player wins!")
		computerLives = computerLives -1
	elif (computer == "lizard"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "rock"):
		print ("player loses!")
		playerLives = playerLives -1		
	elif (computer == "Spock"):
		print ("player loses!")
		playerLives = playerLives -1		
	else:
		print ("It's a tie!")


if (player == "paper"):
	if (computer == "rock"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "Spock"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "lizard"):
		print ("player loses!")
		playerLives = playerLives -1		
	elif (computer == "scissors"):
		print ("player loses!")
		playerLives = playerLives -1		
	else:
		print ("It's a tie!")


if (player == "rock"):
	if (computer == "lizard"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "scissors"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "Spock"):
		print ("player loses!")
		playerLives = playerLives -1		
	elif (computer == "paper"):
		print ("player loses!")
		playerLives = playerLives -1		
	else:
		print ("It's a tie!")


if (player == "lizard"):
	if (computer == "Spock"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "paper"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "scissors"):
		print ("player loses!")
		playerLives = playerLives -1		
	elif (computer == "rock"):
		print ("player loses!")
		playerLives = playerLives -1		
	else:
		print ("It's a tie!")


if (player == "Spock"):
	if (computer == "scissors"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "rock"):
		print ("player wins!")
		computerLives = computerLives -1		
	elif (computer == "paper"):
		print ("player loses!")
		playerLives = playerLives -1		
	elif (computer == "lizard"):
		print ("player loses!")
		playerLives = playerLives -1		
	else:
		print ("It's a tie!")

print("computer lives: " + str(computerLives))
print("player lives: " + str(playerLives))

#for looping!

#if (player == "heal"):
#	playerLives = playerLives + 1
#	print("Player got healed! ")
#	print(str(playerLives))

# add a secret heal function that can add 1 new life to the player! :D
# may need to check heal later
