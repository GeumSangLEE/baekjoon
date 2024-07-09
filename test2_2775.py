import sys

#2층의 3호에 살려면
#1층의 3호까지 사람들 수의 합만큼 사람들을 데려와 살아야 한다
#0층 1 2 3 4
#1층 1 3 6 10 
#2층 1 4 10 20  
#3층 1 5 15 35 호 + (호+층)
#2 3 4 5 (2호라인은 1씩 커짐)
#3 6 10 15 (3호라인은 (3,4,5,6))
#4 10 15 21(4호라인은 (4 5 6))
n = int(sys.stdin.readline())
for _ in range(n):
    floor = int(sys.stdin.readline())
    num = int(sys.stdin.readline())
    f0 = [x for x in range(1,num+1)] #0층
    for f in range(floor): #층 수 만큼 반복
        for n_ in range(1,num):
            f0[n_]+=f0[n_-1]
        print(f0)
    print(f0[-1])



