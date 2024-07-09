import sys
n = int(sys.stdin.readline())
n_len = list(map(int,sys.stdin.readline().split()))

print(min(n_len),max(n_len))