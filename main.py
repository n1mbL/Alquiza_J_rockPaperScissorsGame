from random import randint

# array is just a container, an egg tray. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notation.
choices = ["rock", "paper", "scissors", "lizard", "Spock", "heal"]


# Boolean values are True or False - you can use these to check state and then make programming choices based on their value
player = False

# add player and computer lives
playerLives = 5
computerLives = 5

# defining a win/lose function and invoke it
# in our game loop when lives run out (player or computer)


def winOrLose(status):
	print("called win or lose! You, " + status + "!")
	print("gg")
	print("")
	print("Would you like to play again?")
	choice = input(" Y / N? ")

	global playerLives
	global computerLives
	global player

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


# create an infinite loop (for now) so we can keep playing
while player is False:

	# if (playerLives = 0)
	#	print ("Computer beat you!")
	#else:
	#	print ("You beat the computer!")

	# save the player as a variable called player
	# the value of player will be one of the five choices to type (input)
	
	player = input("Choose rock, paper, scissors, lizard, Spock: ")
	computer = choices[randint(0,4)]

	print("player chose: " + player)
	print("computer chose: " + computer)

	if player == "scissors":
		if computer == "paper":
			print ("player wins!")
			computerLives = computerLives -1
		elif computer == "lizard":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "rock":
			print ("player loses!")
			playerLives = playerLives -1		
		elif computer == "Spock":
			print ("player loses!")
			playerLives = playerLives -1		
		else:
			print ("It's a tie!")


	if player == "paper":
		if computer == "rock":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "Spock":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "lizard":
			print ("player loses!")
			playerLives = playerLives -1		
		elif computer == "scissors":
			print ("player loses!")
			playerLives = playerLives -1		
		else:
			print ("It's a tie!")


	if player == "rock":
		if computer == "lizard":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "scissors":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "Spock":
			print ("player loses!")
			playerLives = playerLives -1		
		elif computer == "paper":
			print ("player loses!")
			playerLives = playerLives -1		
		else:
			print ("It's a tie!")


	if player == "lizard":
		if computer == "Spock":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "paper":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "scissors":
			print ("player loses!")
			playerLives = playerLives -1		
		elif computer == "rock":
			print ("player loses!")
			playerLives = playerLives -1		
		else:
			print ("It's a tie!")


	if player == "Spock":
		if computer == "scissors":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "rock":
			print ("player wins!")
			computerLives = computerLives -1		
		elif computer == "paper":
			print ("player loses!")
			playerLives = playerLives -1		
		elif computer == "lizard":
			print ("player loses!")
			playerLives = playerLives -1		
		else:
			print ("It's a tie!")

	if player == "heal":
		playerLives = playerLives + 1
		print("Player got healed! ")

	print("computer lives: " + str(computerLives))
	print("player lives: " + str(playerLives))
	print("")

	if playerLives == 0:
		# call the winOrLose function here
		winOrLose("lost")


	elif computerLives ==0:
		winOrLose("won")

	# this line below deletes the choice the player made in the previous round
	player = False



	#for looping!



	# add a secret heal function that can add 1 new life to the player! :D
	# may need to check heal later
