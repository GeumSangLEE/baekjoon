import sys
n = (int,sys.stdin.readline())
n_lst = list(map(int,sys.stdin.readline().rstrip()))
sum = 0
for i in n_lst:
    sum += i
print(sum)
