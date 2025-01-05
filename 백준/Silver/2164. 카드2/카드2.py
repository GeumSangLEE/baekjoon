import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())

lst = deque([i for i in range(1,n+1)])
# 1 2 3 4 
while True:
    if len(lst) == 1:
        break
    lst.remove(lst[0]) # 수정하기
    lst.append(lst[0])
    lst.remove(lst[0])
    
    
print(lst[0]) 

