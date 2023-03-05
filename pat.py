def new(n):
	for i in range(n):
		print("*", end="")
		for j in range(1, n):
			if j == i:
				print("*", end="")
			else:
				print("_", end="")
		print("*")
		
print(new(5))