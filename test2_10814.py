import sys

N = int(sys.stdin.readline())
lst = [] 
for _ in range(N):
    old, name = map(str,sys.stdin.readline().split())
    lst.append((int(old),name))

lst.sort(key=lambda x : x[0])
for i in lst:
    print(i[0],i[1])