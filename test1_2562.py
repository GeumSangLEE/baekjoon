import sys
lst = []
for i in range(0,9):
    n = int(sys.stdin.readline())
    lst.append(n)


max_ = max(lst)
idx = int(lst.index(max_))+1
print(idx)