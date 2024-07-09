import sys

n = int(sys.stdin.readline())
answer = 10000


for x in range(1001):
    for y in range(1001):
        if 5*x + 3*y == n:
            answer = min(answer,x+y)
if answer == 10000:
    print("-1")
else:
    print(answer)



