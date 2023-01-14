#print the hckerrank logo 
#using only rjust, ljust and center

thickness = int(input()) #This must be an odd number
c = 'H'

#upper cone
for i in range(thickness):
	print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#upper pillar	
for i in range(thickness+1):
	print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#middle bar	
for i in range((thickness+1)//2):
	print((c*thickness*5).center(thickness*6))  

# lower pillar
for i in range(thickness+1):
	print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)) 
	
#lower cone 	   
for i in range(thickness):
	    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))