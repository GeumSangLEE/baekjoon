import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = list(str(sys.stdin.readline()))
    s.pop(-1)
    sum = 0 
    for j in s:
        if j == '(':
            sum += 1 
        else:
            sum -= 1
            if sum == -1:
                print(sum,'NO')
                break
    if sum > 0:
        print(sum,'NO')
    elif sum == 0:
        print(sum,'YES')
        