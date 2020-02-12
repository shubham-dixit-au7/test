# Question- Write a Python program to accept a filename from the user and print the extension of that. 
			# Sample filename : abc.java
			# Output : java

# Answer-
file_name = input("Enter file name -> ")
file_name = file_name.split(".")
print(file_name[-1])