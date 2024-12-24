import sys
import math
n = int(sys.stdin.readline())
t_size = list(map(int,input().split()))
t,p = map(int,sys.stdin.readline().split())

t_num = 0
for i in t_size:
    if i > t:
        if i == (i // t ):
            t_num += i
        else:
            t_num += math.ceil(i / t)
    elif i == 0:
        t_num += 0
    else:
        t_num += 1
    



pen_block = n // p
pen_one = n % p

print(t_num)
print(pen_block,pen_one)