import os

bin_list = ["make", "gcc", "g++", "java", "python3", "git", "ruby", "irb", "gem", "node"]

for item in bin_list:
	command = item + " --version"
	print(item.center(os.get_terminal_size().columns, '-'))
	os.system(command)