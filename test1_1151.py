

s = input()
s = list(s.upper())

dic = {x:0 for x in s}

for i in s:
    dic[i] += 1

tmp = [k for k,v in dic.items() if max(dic.values()) == v]
if len(tmp) >= 2 :
    print('?')
else: 
    print(tmp[0])

