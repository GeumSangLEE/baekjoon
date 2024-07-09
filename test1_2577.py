cnt = [0]*10
equals = 1
for i in range(3):
    n = int(input())
    equals *= n
    print(equals)
for j in str(equals):
    cnt[int(j)]+=1
for s in cnt:
    print(s)

