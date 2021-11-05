
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# input format will be
# 2
# alfa 23 45 54
# beta 56 45 45
# beta

print("{:.2f}".format(sum(student_marks[query_name][::1])/3))

