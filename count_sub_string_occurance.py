#in this challenge,  the user enters a string and a substring , you are to  print the number of times the substring occurs in the string
#if the string is bananan
#sub_string is nan
#answer should be 2

#asked in hackerrank

string = input("enter a string: ")
sub_string = input("enter a sub_string: ")

arr = []

#appending all the possible sub_strings into arr
for i in range(0, len(string)):	
	for j in range(len(string)-1, i-1, -1):
		arr.append(string[i:j+1])
print(arr.count(sub_string))