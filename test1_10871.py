import sys
N,X = map(int,sys.stdin.readline().split())
min_str = ''
lst=list(map(int,sys.stdin.readline().split()))
for i in lst:
    if i < X:
        i = str(i)
        min_str += i +" "

print(min_str)