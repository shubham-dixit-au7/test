# Question-   Write a Python program to create a dictionary from a string.
# 			Note: Track the count of the letters from the string.
# 			Sample string : 'w3resource'
# 			Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# Answer-

# first method-
# user_input = input("Enter a String ->")
# counts= {}
# for i in user_input:
# 	if not i in counts:
# 		counts[i] = 1
# 	else:
# 		counts[i] += 1
# print(counts)


# Second method-
user_input = input("Enter a String -> ")
counts= {}

for i in user_input:
	counts[i]=counts.get(i,0) + 1
print(counts)

