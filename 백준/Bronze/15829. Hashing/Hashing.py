import sys

r = 31

l = int(sys.stdin.readline())
s = list(str(sys.stdin.readline().strip()))

result = 0
for i,s in enumerate(s):
    result += (ord(s)-96) * (r**i)
print(result)