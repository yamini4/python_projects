# arrays: arrays are used to store data of just one type
# they have index which is used to access the data according to index
import array as arr

ar1 = [[1, 2, 3], [4, 5, 6]]    # 2-D array

ar = arr.array('i', [1, 2, 3, 4, 5])
while True:
    print('1. print array')
    print('2. Add elements')
    print('3. delete elements')
    print('4. exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        print('the array elements are:')
        for number in ar:
            print(number, end=" ")
        print("\n")
    elif choice == 2:
        val = int(input('please enter the integer number:'))
        if isinstance(val, int):
            ar.append(val)
    elif choice == 3:
        value = ar.pop()
        print('the value deleted was:', value)
    elif choice == 4:
        break
    else:
        print("Enter valid choice.")




