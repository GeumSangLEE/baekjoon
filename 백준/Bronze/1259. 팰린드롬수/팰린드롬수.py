import sys

lst = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        n_str = str(n)
        if n_str == n_str[::-1]:
            lst.append('yes')
        else:
            lst.append('no')
for i in lst:
    print(i)







