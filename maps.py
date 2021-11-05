# ChainMap is a type of data structure
# which is used to manage multiple dictionaries together

import collections

dict1 = {'day1': 'mon', 'day2': 'tue'}
dict2 = {'day3': 'wed', 'day4': 'thur'}
dict3 = {'day5': 'fri', 'day6': 'sat', 'day7': 'sun'}

res = collections.ChainMap(dict1, dict2, dict3)

# creating a single dictionary

print(res.maps, '\n')

print('keys = {}'.format(list(res.keys())))
print('values = {}'.format(list(res.values())))
print("\n")

# print all elements from the result
print("elements:")
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# finding a specific value in result
print('day3 in res: {}'.format(('day3' in res)))
print('day2 in res: {}'.format(('day2' in res)))

res1 = collections.ChainMap(dict3, dict2, dict1)
print(res1.maps, "\n")



