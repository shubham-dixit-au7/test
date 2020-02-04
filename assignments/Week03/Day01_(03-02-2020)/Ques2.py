# Question- Write a Python program to combine two dictionary adding values for common keys.
#			d1 = {'a': 100, 'b': 200, 'c':300}
#			d2 = {'a': 300, 'b': 200, 'd':400}
#			Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# Answer-
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print("First Dictionary -> ", d1)
print("Second Dictionary ->", d2)
d2lst = list(d2.keys())
d1lst = list(d1.keys())
for i in d2lst:
	if i not in d1lst:
		newKey = i
d3 = {}
d3.update(d1)
d3[newKey] = 0
for key, value in d3.items():
	for key1 , value1 in d2.items():
		if(key == key1):
			value = value + value1
			d3[key] = value
		else:
			pass
print("Merged Dictionary ->", d3)