# sets are mutable
# sets are un_ordered collection of unique elements
set1 = {1, 7, 6, 2, 3}
print(set1)

# add(to add elements
set1.add(8)
print(set1)

set2 = {4, 5, 6, 4, 3, 9}


# union(), intersection(), difference(), symmetric_difference()


print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

print(set1.symmetric_difference(set2))

