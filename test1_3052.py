import sys
lst = []
for i in range(10):
    n = int(sys.stdin.readline())
    diveision = n % 42
    lst.append(diveision)
print(len(set(lst)))