'''
[아이디어]
움직이는 패턴이 있음. 그리고 잘 보면 그냥 더한거 -1 이런식으로 움직인다는 걸 알 수 있음
1 +2 1/1 처음 수
2 +3 1/2 2/1
3 +4 3/1 2/2 1/3
4 +5 1/4 2/3 3/2 4/1
좀 이상하게 풀었음, 시간도 오래 걸렸고
'''

import sys
input=sys.stdin.readline
N=int(input())
a,b=1,1 # 초기값
n=1
if N>=2:
    k=2
    a,b=1,2
    for _ in range(2,N):
        if k%2==1 and a==1:
            a=1
            b=k+1
            k+=1

            continue
        if k%2==0 and b==1:
            a=k+1
            b=1
            k+=1

            continue
        if k%2==1:
            a-=1
            b+=1
        else:
            a+=1
            b-=1
print(f"{a}/{b}")