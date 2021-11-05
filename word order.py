from collections import OrderedDict

d = OrderedDict()
n = int(input())
for i in range(n):
    s = input()
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1

print(len(d.keys()))

print(' '.join([str(d[k]) for k in d.keys()]))


# example for dictionaries(stdin, stdout)
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(d.items())
print(d.keys())
print(d.values())
print(' '.join([str(d[k]) for k in d.keys()]))

s1 = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4)]
d1 = defaultdict(set)
for k, v in s1:
    d1[k].add(v)

print(d1.items())
print(d1.keys())
print(d1.values())
