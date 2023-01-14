#given a string s and an integer k , reverse the first k character for every 2k characters counting from the start of the string 

#example "abcd" it should return "bacd"
#or "efghij" it should return "feghji"

#asked in leetcode

s = "abcdefghijklmno"
k = 2
arr = [i for i in s]
for i in range(0, len(s), 4):
	n = arr[i]
	arr[i] = arr[i+1]
	arr[i+1] = n
output = "".join(arr)
print(output)	