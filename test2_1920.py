import sys 

n = int(sys.stdin.readline()) #n
n_num = list(map(int,sys.stdin.readline().split())) #n의 수들
n_num.sort()
m = int(sys.stdin.readline())
m_num = list(map(int,sys.stdin.readline().split()))
    

def binary_search(data,data2):
    for i in data2:
        start = 0
        end = len(data) - 1
        while start <= end:
            mid = (start + end) //2 #중간값
            if  data[mid] > i: #target이 작으면 왼쪽을 더 탐색
                end = mid -1
            elif data[mid] < i: #target이 크면 오른쪽을 더 탐색
                start = mid + 1
            else:
                start = mid
                end = mid
                break
        if start == mid and end == mid:
            print(1)
        else:
            print(0)
binary_search(n_num,m_num)
