#Question- https://www.hackerrank.com/challenges/python-string-formatting/problem


#Answer-
def print_formatted(number):
    # your code goes here
    width = (len(bin(number))-2)
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)
        binary = bin(i)
        hexadecimal = hex(i)
        print(decimal.rjust(width), octal[2:].rjust(width), hexadecimal[2:].rjust(width), binary[2:].rjust(width)) 

number = int(input("enter the no. of lines -> "))
print_formatted(number)