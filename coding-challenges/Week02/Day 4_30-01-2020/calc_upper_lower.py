#Question- Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

#Answer-

def countUpperCase(string):
	upper= 0
	for i in string:
		if(i.isupper()):
			upper=upper+1
	return upper	

def countLowerCase(string):
	lower= 0
	for i in string:
		if(i.islower()):
			lower=lower+1
	return lower


string = input("Enter a String -> ")
upper = countUpperCase(string)
lower = countLowerCase(string)
print("Total no. of uppercase characters present in string are " , upper)
print("Total no. of lowercase characters present in string are " , lower)