import sys

m,n = map(int,sys.stdin.readline().split())
lst = []
for i in range(m,n+1):
    cnt = 0
    for k in range(2,i // 2+1):
        if i % k == 0:
            cnt += 1
            break
    if cnt == 0:
        print(i)

