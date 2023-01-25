#the first line should print true if any of the inputed string is alnum
#the second line should print true if any of the inputed string is alpha
#third line print True if any is digit 
#fourth print true if any is lower
#fifth print true if any is upper 

#that should be the format of the output in only five lines

name = input("enter a word: ")
s_let = []
cap_let = []
dig = []

for i in name:
	if i.islower():
		s_let.append(i)
	elif i.isupper():
		cap_let.append(i)
	elif i.isdigit():
		dig.append(i)
		
if s_let != [] or cap_let !=[] or dig != []:
	print(True)
else:
	print(False)
if s_let != [] or cap_let != []:
	print(True)
else:
	print(False)
if dig != []:
	print(True)
else:
	print(False)
if s_let != []:
	print(True)
else:
	print(False)
if cap_let != []:
	print(True)
else:
	print(False)