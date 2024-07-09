import sys
n = int(sys.stdin.readline())

'''
1234 (1) = 234
342 (3) = 42
24 (2) =4
4
'''

lst = [i for i in range(1,n+1)]
pass_card = []
try:
    for _ in range(n):
        pass_card.append(lst[0])
        del lst[0]
        lst.append(lst[0])
        del lst[0]
except:
    pass

for j in pass_card:
    print(j, end = " ")
    
