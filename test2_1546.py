import sys
n = int(sys.stdin.readline())

# score / maxscore * 100
sum = 0

s = list(map(int,sys.stdin.readline().split()))
max_ = max(s) #최고 점수
for k in s:
    sum += (k/max_*100)
print(sum / n)
