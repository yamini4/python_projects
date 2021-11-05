N = int(input())
d = []
for i in range(N):
    command = input().split()
    if command[0] == "sort":
        d.sort()
    elif command[0] == "print":
        print(d)
    elif command[0] == "reverse":
        d.reverse()
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "insert":
        d.insert(int(command[1]), int(command[2]))
    elif command[0] == "append":
        d.append(int(command[1]))
    else:
        d.remove(int(command[1]))

