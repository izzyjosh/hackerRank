#write a funcrion to pront the index whose value sum up to give the specified value

#for example the arr [1, 2, 3, 4] target = 7 it should print [2, 3]

def return_index_sum(arr:list, k:int) -> list:
	index = []
	for i in range(len(arr)):
		for j in range(len(arr)-1, i, -1):
			if arr[i] + arr[j] == k:
				index.append(i)
				index.append(j)
	return index

print(return_index_sum([1, 2, 3, 5, 6, 6], 11))