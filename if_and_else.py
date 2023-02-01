num = int(input("enter a positive integer: "))
if num % 2 == 1:
	print("Weird")
else:
	if num < 5:
		print("Not Weird")
	elif num > 5 and num <= 20:
		print("Weird")
	elif num > 20:
		print("Not Weird")