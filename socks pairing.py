import os


def sockmerchant(n, ar):
    flag = 0
    ar.sort()
    i = 0
    while i < n-1:
        if ar[i] == ar[i+1]:
            flag = flag+1
            i += 2
        else:
            i += 1
    return flag


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    result = sockmerchant(n, ar)
    fptr.write(str(result) + '\n')

    fptr.close()


