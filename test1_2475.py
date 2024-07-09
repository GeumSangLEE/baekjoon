import sys
n = list(map(int,sys.stdin.readline().split()))
sum = 0
for i in n:
    sum += i*i
print(sum % 10)

