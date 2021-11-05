# lists are mutable
list1 = [1, 2, 3, 'yamini', (2, 0), 26]

# extend() and insert(), append()
list1.extend((2, 0))
print(list1)
list1.insert(3, 'age')
list1.insert(1994, 'DOB')
print(list1)
list1.append((5, 3))
list1.append(3)
print(list1)

# del, pop(), remove()


del list1[3]
print(list1)
a = list1.pop(4)
print(a)
list1.remove(2)
print(list1)
print(list1[::-1])
print(list1[::2])


# difference between sort, sorted

# sorted

list2 = [1, 24564, 36, 36, 534, 7656, 403957]
print(sorted(list2))
print(list2)

# sort, index, count

list2.sort(reverse=True)
print(list2)
print(list2.index(24564))     # to print the index of 24564
print(list2.count(36))
print(list2.count(534))




