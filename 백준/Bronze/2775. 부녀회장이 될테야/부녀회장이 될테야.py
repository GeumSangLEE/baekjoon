import sys

T = int(sys.stdin.readline())

lst = []
k_n = []

k_max = 0
for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    k_n.append([k,n])
    if k_max < k:
        k_max = k
        
    
for i in range(k_max+1):
    l = []
    for j in range(1,15):
        if i == 0:
            l.append(j)
        else:
            partial_sum = sum(lst[i-1][:j])
            l.append(partial_sum)
    lst.append(l)
 
for k,n in k_n:
    print(sum(lst[k-1][:n]))
                
        
            
            
            

