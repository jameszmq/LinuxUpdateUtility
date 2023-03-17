import os

def apt_update():
	prompt = "Updating apt"
	print(prompt.center(os.get_terminal_size().columns, '-'))
	os.system("sudo apt-get update")
	os.system("sudo apt-get full-upgrade")
	os.system("sudo apt-get autoremove")
	os.system("sudo apt-get autoclean")

def yum_update():
	prompt = "Updating yum"
	print(prompt.center(os.get_terminal_size().columns, '-'))
	os.system("sudo yum update")

def pacman_update():
	prompt = "Updating pacman"
	print(prompt.center(os.get_terminal_size().columns, '-'))
	os.system("sudo pacman -Syu")

def pip_update():
	prompt = "Updating pip"
	print(prompt.center(os.get_terminal_size().columns, '-'))
	os.system("python3 -m pip list --outdated > a.txt")
	fp = open("a.txt", "r")
	lines = fp.readlines()
	if len(lines) > 2:
		lines.pop(0)
		lines.pop(0)
		result = ""
		for line in lines:
			if line != "":
				command = "python3 -m pip install --upgrade " + line.split()[0]
				print(command)
				os.system(command)
	else:
		print("Nothing to update.")
	fp.close()
	os.system("python3 -m pip cache purge")
	os.remove("a.txt")

def gem_update():
	prompt = "Updating gem"
	print(prompt.center(os.get_terminal_size().columns, '-'))
	os.system("sudo gem update")

def exit_update():
	print("Thanks for using. Bye!")
	exit(0)

def prompt():
	print("Please select the upgrade you want to run:")
	for option in option_list:
		print(option[0] + ". " + option[1])
	selection = input('Selection: ').lower()
	for char in selection:
		for option in option_list:
			if char == option[0]:
				option[2] = True
	for option in option_list:
		if option[2]:
			option[3]()
			option[2] = False
	prompt = "Done Updating"
	print(prompt.center(os.get_terminal_size().columns, '-'))

option_list = [
	["1", "pip", 		False, pip_update],
	["2", "gem", 		False, gem_update],
	["3", "apt", 		False, apt_update],
	["4", "yum", 		False, yum_update],
	["5", "pacman", 	False, pacman_update],
	["6", "exit", 		False, exit_update]
]

try:
	print("Welcome to the Linux Upgrade Utility!")
	while True:
		prompt()
	exit(0)
except KeyboardInterrupt:
	print("\nCtrl + C received. Exiting.")
	exit(0)