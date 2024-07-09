import sys
n = int(sys.stdin.readline())

num = 1

for i in range(n):
    num += i*6
    print('num',num)
    if n <= num:
        print(i)
