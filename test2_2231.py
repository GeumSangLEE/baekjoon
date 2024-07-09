import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    num = sum(map(int,str(i))) #숫자 각각의 합
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    #생성자가 없는 경우
    if i == n:
        print(0)
        break