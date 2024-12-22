import sys

lst = []
while True:
    one,two,thr = map(int,sys.stdin.readline().split())
    if (one + two + thr) == 0:
        break
    else:
        if (one **2) + (two **2) == (thr **2):
            lst.append("right")
        elif (two **2) + (thr **2) == (one **2):
            lst.append("right")
        elif (one **2) + (thr **2) == (two **2):
            lst.append("right")
        else: 
            lst.append('wrong')
for i in lst:
    print(i)
lst = []
            
        
