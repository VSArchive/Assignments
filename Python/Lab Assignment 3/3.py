vowels = open("vowels.txt", "a")
cons = open("cons.txt", "r")

vowels.write(cons.read())
