#!/usr/bin/python3

print("Welcome to my computer acronym game.")

play = input("Would you like to play? ")

if play.lower() != "yes":
	quit()

print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
	print("Correct!")
	score += 1
else: 
	print("Sorry, that is incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
	print("Correct!")
	score += 1
else: 
	print("Sorry, that is incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
	print("Correct!")
	score += 1
else: 
	print("Sorry, that is incorrect!")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
	print("Correct!")
	score += 1
else: 
	print("Sorry, that is incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score/4) * 100) + "%.")

print("Thank you for Playing!")
