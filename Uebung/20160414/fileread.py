file = open("fileread.txt", "r")
dict = {}

for line in file:
	splitted = line.split(":")
	dict[splitted[0]] = splitted[1]

print(dict)
		



