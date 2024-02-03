#!/usr/bin/python3

from cryptography.fernet import Fernet

def load_key()
	file = open("key.key", "rb")
	key = file.read()
	file.close()
	return key

key = load_key()
fer = Fernet(key)

#def write_key():
#	key = Fernet.generate_key()
#	with open("key.key", "wb") as key_file:
#		key_file.write(key)

#Three Modes here: 'a', 'r', and 'w'
#'a' will append to the end of the file and create the file if it does not exist.	
#'r' will not write anything. It only reads.
#'w' will overwrite the file everytime it is opened.

def view():
	with open("passwords.txt", "r") as f:
		for line in f.readlines():
			data = (line.rstrip())
			user, passw = data.split("|")
			print("Username: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
	username = input("Username: ")
	password = input("Password: ")

	with open("passwords.txt", "a") as f:
		f.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
	mode = input("Would you like to view existing passwords, or add a new one (view, add), enter q to quit? ").lower()
	if mode =="q":
		break
	elif mode == "view":
		view()
	elif mode == "add":
		add()
	else:
		print("You have selected an invalid option.")
		continue