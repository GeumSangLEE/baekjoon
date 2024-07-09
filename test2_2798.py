
import sys
#n,m = map(int,sys.stdin.readline().split())
card_n = [1,2,3,4]


for i in card_n:
    s = 0

path = [0]*3
lst = []
def dfs(level, start):
		# 3장 모두 뽑았으면 출력하고 리턴
    if level == 3:   
        lst.append(list(path)) 
        return
    for i in range(start, 4):
        path[level] = card_n[i]  # 카드 뽑기
        print(f"Selected card at level {level}: {path}")
        dfs(level + 1, i + 1)    # 직전에 뽑은 카드의 다음 인덱스의 카드부터 카드 뽑기
        path[level] = 0          # 리턴 이후 뽑은 카드 초기화
        print(f"Reset card at level {level}: {path}")
        
dfs(0, 0)       
'''
dfs(0, 0)
number = []
for k in lst:
    sum = 0
    for j in k:
        sum += j
    if sum <= m:
        number.append(sum)

print(max(number))
'''