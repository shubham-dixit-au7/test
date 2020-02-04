# Question- Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Answer-

user_input = int(input("Enter a Number -> "))
d = dict()

for i in range(1 , user_input + 1):
	d[i] = i ** 2
print(d)
