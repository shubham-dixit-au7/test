# Question- Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
			# Sample data : 3, 5, 7, 23
			# Output :
			# List : ['3', ' 5', ' 7', ' 23']
			# Tuple : ('3', ' 5', ' 7', ' 23')

# Answer-

data = input("Enter the sequence (comma-separated) ->")
lst = data.split(",")
print("List -> ", lst)
tpl = tuple(lst)
print("Tuple -> ", tpl)