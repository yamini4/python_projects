n = int(input())

if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")

