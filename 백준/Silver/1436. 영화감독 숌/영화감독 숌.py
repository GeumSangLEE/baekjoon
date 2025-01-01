import sys

n = int(sys.stdin.readline())

total = 0
result = None
for i in range(666,1000000000):
    if '666' in str(i):
        total += 1
        result = i
        if total == n:
            break
print(result)