#!/usr/bin/python3

import random

print("Welcome to my random number game!")

#Just for my own notes: You can use random.randrange(0,10)
#If you do this, numbers 0 and 10 will not be included.
#The range will include numbers 1 through 9.
#If you do random.randint and it will include the range numbers you specify.
#If you enter (0, 10) both of those digits will be included as well.

top_of_range = input("Please enter a number: ")

if top_of_range.isdigit():
	top_of_range = int(top_of_range)

	if top_of_range <= 0:
		print("Please enter a number greater than 0.")
		quit()

else:
	print("Please enter a number.")
	quit()

random_number = random.randint(0, top_of_range)
number_of_guesses = 0

while True:
	number_of_guesses += 1
	user_guess = input("Please guess what the random number is: ")

	if user_guess.isdigit():
		user_guess = int(user_guess)

	else:
		print("Please enter a number next time.")
		continue

	if user_guess == random_number:
		print("That is Correct! You have guessed the random number.")
		break

	elif user_guess > random_number:
		print("That is above the random number.")

	else:
		print("That is below the random number,")

print("It took you", number_of_guesses, "To guess the correct random number!")
