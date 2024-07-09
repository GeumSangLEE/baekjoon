import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0]=='push':
        lst.append(int(s[1]))
    elif s[0] == 'pop':
        if len(lst) != 0:
            print(lst[-1])
            del lst[-1] 
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(lst))
    elif s[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
