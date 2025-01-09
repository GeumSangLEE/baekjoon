import sys

m = int(sys.stdin.readline())


s = set([])
for _ in range(m):
    input_ = sys.stdin.readline().strip().split()
    if len(input_) == 2:
        num = int(input_[1])
    else:
        num = None
        
    if input_[0] == 'add':
        s.add(num)
    elif input_[0] == 'remove':
        s.discard(num)
    elif input_[0] == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif input_[0] == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif input_[0] =='all':
        s.clear()
        s = {i for i in range(1,21)}
    elif input_[0] == 'empty':
        s.clear()

        