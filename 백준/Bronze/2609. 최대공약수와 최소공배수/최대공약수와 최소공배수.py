'''
[아이디어]
1. 최대공약수
EX) 18 42: 최대공약수가 6이란 건 바로 알 수 있는데, 함수로?
방법1. 1~a까지 쭉 순회하면서 리스트에 넣고 맥스 값 출력하기

2. 최소공배수
EX) 12 18
방법1. b*1,b*2.. 등을 진행해 나가면서 다른 수로 나누어 지면 된다.

이 방법은 일단 하나씩 때려 박으면서 답을 도출하는 방법
'''
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
if a>=b:
    max,min=a,b
else:
    max,min=b,a
# 최대공약수 (다 때려넣기 방식)
gcd=[]
for i in range(1,min+1): # 주의
    if min%i==0 and max%i==0:
        gcd.append(i)
ans1=gcd[-1]
# 최소공배수
k=1
Target=max
while True:
    if max%min==0:
        break
    else:
        max=Target*k
        k+=1
ans2=max
print(ans1)
print(ans2)