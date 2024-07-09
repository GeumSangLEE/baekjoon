import sys

a,b = map(int,sys.stdin.readline().split())
#
#두 자연수의 곱  = 최대 공약수 x 최소 공배수
#최소공배수 = 두 자연수의 곱 / 최대 공약수
#유클리드 호제법 (유클리드 알고리즘)
#호제법 = 두 수가 서로 상대방 수를 나누어서 결국 원하는 
#수를 얻는 알고리즘

def gcd(a,b):
    if b == 0:
        pass

