#Question- Write a Python function that takes a number as a parameter and check the number is prime or not. 


#Answer-

def isPrime(user_input):
	if (user_input == 1):
		return False
	else:
		for i in range(2, user_input):
			if((user_input % i) == 0):
				return False
		return True
	

user_input = int(input("Enter a Number -> "))
result = isPrime(user_input)
if (result):
	print(result)
	print("The number which you entered is prime")
else:
	print("The number which you entered is not prime")