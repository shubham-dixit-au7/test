# Question- Write a Python program to sort (ascending and descending) a dictionary by value. [use sorted()]

# Answer-

#First Method-
# fruits = {"Orange":2 , "Banana": 3, "Mango":6 ,"Papaya":1, "Guava": 4}
# new_fruits = dict()
# for key , value in fruits.items(): 
# 	new_fruits[value] = key

# print("Original List of Items present in dictionary are ->", new_fruits.items())
# print("Sorted List of Items in ascending order present in dictionary are ->",  sorted(new_fruits.items()))
# print("Sorted List of Items in descending order present in dictionary are ->", sorted(new_fruits.items(), reverse= True) )


#Second Method-
def take_second(elem):
    return elem[1]


fruits = {"Orange":2 , "Banana": 3, "Mango":6 ,"Papaya":1, "Guava": 4}
print("Original List of Items present in dictionary are ->", fruits.items())
print("Sorted List of Items in ascending order present in dictionary are ->",  sorted(fruits.items(), key=take_second))
print("Sorted List of Items in descending order present in dictionary are ->", sorted(fruits.items(), key=take_second , reverse= True) )