

if __name__ == '__main__':
    n = int(input())
    arr1 = map(int, input().split())

arr2 = set(arr1)
print(sorted(arr2)[-2])

print(sorted(set(arr1))[-2])

