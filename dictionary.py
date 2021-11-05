# dictionaries, sets, lists and tuple are in_built data structures
# dictionaries, sets, lists are mutable && tuples are immutable


# dictionaries are mutable
# it holds key, value pair
dict1 = {1: 'java', 2: 'python'}
print(dict1)
print(dict1.keys())
print(dict1.values())
# replaces elements to dictionary
dict1[1] = 'C'
print(dict1)
# adding elements in dictionary
dict1[3] = 'MATLAB'
print(dict1)
list1 = ['yamini', 'naveen', 'mental', 'gotta']
list2 = [1, 2, 3, 4]
dict2 = {}

for j in range(len(list2)):
    dict2[list2[j]] = list1[j]

print(dict2)

# del

del dict1[1]
print(dict1)
del dict2[4]
print(dict2)

# pop

print(dict2.pop(3))
print(dict2)

# popitem item(it removes last element in the dict)

print(dict1.popitem())
print(dict1)
