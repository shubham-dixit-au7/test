# Question- Write a Python program which accepts the radius of a circle from the user and compute the area. 
# 			Sample Output :
# 			r = 1.1
# 			Area = 3.8013271108436504

# Answer-
from math import pi 
def areaCircle(radius):
	area =  pi * radius ** 2
	return area

radius = float(input("Enter radius of circle ->")) 
area = areaCircle(radius)
print(area)