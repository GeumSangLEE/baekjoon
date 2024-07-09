import sys
A,B,V =map(int,sys.stdin.readline().split())
sum = 0
day = 0
while True:
    day += 1
    sum  += A
    sum -= B
    if sum == V:
        day-=1
    if sum >= V:
        print(day)
        break
