"""
this question was asked in harker rank
you code should be dynamic
"""

print("dimension should be in the format of (row  column)\n")

print("""NOTE : 
dimension[0] must be an odd number
dimension[1] must also be an odd number and a multiple of 3.\n""")

dimension = input("dimension: ").split(" ")
sign = ".|."
n = 1
for i in range(int(dimension[0])):

	print(sign.center(int(dimension[1]), "-"))
	if int(dimension[1]) - (len(sign)) == 6:
		break
	sign += ".|..|."
	n += 2		
print("welcome".center(int(dimension[1]), "-"))
sign = ".|."
for j in range(i+1):
	print((sign * n).center(int(dimension[1]), "-"))
	n -= 2
	