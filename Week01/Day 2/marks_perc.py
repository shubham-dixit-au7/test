#Question- write a program that takes input from the user as marks in 5 subjects and assigns a grade according to the following rules:
#           Perc = (s1+s2+s3+s4+s5)/5.
#           A, if Perc is 90 or more
#           B, if Perc is between 70 and 90(not equal to 90)
#           C, if Perc is between 50 and 70(not equal to 70)
#           D, if Perc is between 30 and 50(not equal to 50)
#           E, if Perc is less than 30

#Answer-
s1=int(input("Enter the Marks of First Subject-"))
s2=int(input("Enter the Marks of Second Subject-"))
s3=int(input("Enter the Marks of Third Subject-"))
s4=int(input("Enter the Marks of Fourth Subject-"))
s5=int(input("Enter the Marks of Fifth Subject-"))
perc=(s1+s2+s3+s4+s5)/5
if (perc >= 90):
    print("Grade A")
elif (perc >= 70):
    print("Grade B")
elif (perc >= 50):
    print("Grade C")
elif (perc >= 30):
    print("Grade D")
elif(perc < 30):
    print("Grade E")
else:
    print("Invalid Input.")