
from numpy import *
a = array([['MON', 23, 44, 35, 54], ['TUE', 43, 54, 54, 34], ['WED', 47, 55, 45, 78]])
print(type(a))
for r in a:
    for c in r:
        print(c, end=" ")
    print("")

print(a[2])
print(a[1][2])

# append(ndarray,[row],0)

a_r = append(a, [['AVG', 45, 54, 75, 54]], 0)
print(a_r)

# delete(a, [index], 0)

print("after deletion of a row in a matrix")
a_r = delete(a_r, [2], 0)
print(a_r)

# update row in matrix

a_r[2] = ['WED', 45, 65, 46, 34]
print("updated matrix")
print(a_r)

