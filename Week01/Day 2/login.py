# Question- Build a very basic login system that takes in input from the username password. checks if username is "Priyesh" and password is "password" and responds with:
#               -Username Does not Exist
#               -Passwords do not match
#               -Entered the System

# Answer-
user_name = input ("Enter the Username:")
if(user_name == "Priyesh"):
    password = input ("Enter the Password:")
    if(password == "password"):
        print("Entered the System")
    else:
        print("Passwords do not match")
else:
    print("Username Does not Exist")