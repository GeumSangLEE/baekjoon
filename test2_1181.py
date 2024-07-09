#단어 정렬
import sys

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    s = input()
    if s not in lst:
        lst.append(s)

lst.sort(key=lambda x:len(x))
lst.sort()

for S in lst:
    print(S)

