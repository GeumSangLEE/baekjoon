import sys
import re 
# 3의 배수 o 5의 배수 x = FizzBuzz
# 3의 배수 o 5의 배수 x = Fizz
# 3의 배수 x 5의 배수 o = Buzz
# 3의 배수 x 5의 배수 x = i

lst = []
for n in range(3):
    input_ = input()
    p = re.compile('[0-9]+')
    m= p.match(input_)
    if m:
        input_ = int(input_)
    
    lst.append(input_)

num = None
index = None

for i,s in enumerate(lst):
    lst_2 = []
    if type(s) == int:
        num = s
        index = i

if index == 0:
    num += 3
elif index == 1:
    num += 2
elif index == 2:
    num += 1


if (num % 3 == 0) and (num % 5 == 0):
    print('FizzBuzz')
elif (num % 3 == 0) and (num % 5 != 0):
    print('Fizz')
elif (num % 3 != 0) and (num % 5 == 0):
    print('Buzz')
else:
    print(num)
        