import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)
lst.sort()
for j in lst:
    print(j)