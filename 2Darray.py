from numpy import *
arr1 = array([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])

sum1 = array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
top = 0
bot = 0
mid = 0
for i in range(0, 6):
    for j in range(0, 6):
        print(arr1[i][j], end=" ")
    print("\n")


for i in range(0, 4):
    for j in range(0, 4):
        top = arr1[i][j]+arr1[i][j+1]+arr1[i][j+2]
        mid = arr1[i+1][j+1]
        bot = arr1[i+2][j]+arr1[i+2][j+1]+arr1[i+2][j+2]
        sum1[i][j] = top+bot+mid
        print(sum1[i][j], end=" ")
    print("\n")


val = 0
for element in range(4):
    for values in range(4):
        if sum1[element][values] >= val:
            val = sum1[element][values]

print("maximum value: ", val)

