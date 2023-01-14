#standard leap year checker 
#years which are divisible by 4 and are also divisible by 100
#must be divisible by 400 for it to be a leap year
#but if the year is only divisible by 4 it is a leap year.


year = int(input("year: "))

if year % 4 == 0 and year % 100 == 0:
	if year % 400 == 0:
		print(True)
	else:
		print(False)
elif year % 4 == 0:
	print(True)
else:
	print(False)