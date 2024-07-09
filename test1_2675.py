import sys
n= int(sys.stdin.readline())

for i in range(n):
    num,s = map(str,sys.stdin.readline().split())
    s = list(s)
    s_ = ''
    for j in s:
        s_ += j*int(num)
    print(s_)
        