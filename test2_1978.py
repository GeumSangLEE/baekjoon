import sys
n = int(sys.stdin.readline())
num = map(int,sys.stdin.readline().split())

sum  = 0

for k in num:
    s = 0
    for i in range(1,1000):
        if k % i == 0:
            s += 1 
    if s == 2:
        sum += 1
print(sum)



                