import array as arr

a = arr.array('i', [1, 2, 3])

print("Array before insertion: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print("\n")
a.insert(1, 4)
print("Array after insertion: ", end=" ")
for i in range(0, 4):
    print(a[i], end=" ")




