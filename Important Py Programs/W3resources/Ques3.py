#Question- Write a Python program to display the current date and time.

#Answer-
import datetime
now =datetime.datetime.now()
print ("Current Date and time -> ",now.strftime("%Y-%m-%d %H:%M:%S"))
