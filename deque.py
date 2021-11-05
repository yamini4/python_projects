import collections
Double_ended = collections.deque(["monday", "tuesday", "wednesday"])

Double_ended.append("thursday")

print("appended at right:   ")
print(Double_ended)

Double_ended.appendleft("sunday")

print("appended at right at left is:   ")
print(Double_ended)

Double_ended.pop()

print("deleting from right:   ")
print(Double_ended)

Double_ended.popleft()

print("deleting from left:   ")
print(Double_ended)

