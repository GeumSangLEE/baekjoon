import sys

n = int(sys.stdin.readline())

que = []
for _ in range(n):
    s = sys.stdin.readline().strip().split()
    if len(s) == 2:
        que.append(s[1])
    elif s[0] == 'pop':
        if que == []:
            print(-1)
        else:
            pop_ = que.pop(0)
            print(pop_)
    elif s[0]  == 'size':
            print(len(que))
    elif s[0]  == 'empty':
        if que == []:
            print(1)
        else:
            print(0)
    elif s[0]  == 'front':
        if que == []:
            print(-1)
        else:
            print(que[0])
    elif s[0]  == 'back':
        if que == []:
            print(-1)
        else:
            print(que[-1])
        
    