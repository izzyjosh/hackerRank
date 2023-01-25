#you are given an array representing a row of seat where
#seat[i]  = 1 represent a person seating at the ith seat
#seat[i] = 0 represent that the ith  seat is empty

#there is atleast one empty seat and atleast one occupied seat

#Alex want to sit in the seat such that the closest distance between him and the closest person is maximized

#Return the maximum distance to the closest person

def max_dist_to_closest_person(arr:list) -> int:
	
	o_sit = []
	o_sit.insert(0, 0)
	
	for i in range(len(arr)):
		if arr[i] == 1:
			o_sit.append(i)
			
	if len(o_sit) > 2:
		empty = [o_sit[i+1] - o_sit[i] for i in range(len(o_sit)-1)]
		
		max = empty[0]
		for i in empty:
			if i > max:
				max = i
		max_dist = int(max/2)
		
		for i in range(len(o_sit)-1):
			if o_sit[i+1] - o_sit[i] == max:
				n = o_sit[i+1]
				
		print(f"maximum distance = {max_dist}")
		print(f"seat number = {n - max_dist}")
		
		
	else:
		n = arr.index(1)
		if n > len(arr)/2:
			print(f"maximum distance = {n - 0}")
		elif n < len(arr)/2:
			print(f"maximum distance = {len(arr)-1-n}")


max_dist_to_closest_person([ 1,  0, 1, 0, 0,0, 0, 0, 0, 0, 0, 1])