from array import *
a = [[11, 12, 13, 32], [23, 54, 34], [10, 34, 8, 9], [12, 33, 4, 6]]
for r in a:
    for c in r:
        print(c, end=" ")
    print()
print(type(a))
print(a[0][1])
