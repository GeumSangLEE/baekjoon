import sys
n = int(sys.stdin.readline())
for i in range(n):
    h,w,num = map(int,sys.stdin.readline().split())
    r = num % h
    rr = (num // h) +1
    if  r == 0:
        r = h
        rr = rr -1
        print(rr)
    else:
        r = r
        if rr <= 9:
            s = str(r) + '0' + str(rr)
        else:
            s = str(r) + str(rr)        
        print(int(s))