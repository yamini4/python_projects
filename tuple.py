# tuples are immutable(changing data is not allowed)
tup1 = (3, 4, 5)
print(tup1)
# tuple concatenation
tup1 = tup1 + (1, 2, 3)
print(tup1)
tup2 = (6, 7, 8)
tup2 = tup2 + tup1

print(tup2)


