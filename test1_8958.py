import sys
n = int(sys.stdin.readline())


for j in range(n):
    sum = 0
    plus = 0
    quize = input()
    for i in quize:
        if i == "O":
            sum += 1
            sum += plus
            plus += 1

        else:
            plus *= 0
    print(sum)