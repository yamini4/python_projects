def findposition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n*i
        i += 1

    return


print("position of n th multiple of k in fibonacci series is", findposition(4, 5))

