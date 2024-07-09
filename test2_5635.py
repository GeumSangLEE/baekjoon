import sys 

n = int(sys.stdin.readline())
lst_1 = []
name = []

for _ in range(n):
    student = sys.stdin.readline().strip()
    s = student.split()
    lst_1.append(s[1:])
    name.append(s[0])

result = []
day = [] 
for idx,i in enumerate(lst_1):
    if len(i[-1]) == 1:
        i[-1] = '0' + i[-1]
    elif len(i[0]) == 1:
        i[0] = '0' + i[0]
    elif len(i[1]) == 1:
        i[1] = '0' + i[1]
    p = i[-1]+i[1]+i[0]

    result.append((name[idx],int(p)))
result.sort()
print(result)
print(result[0][0],result[-1][0],sep = '\n')
