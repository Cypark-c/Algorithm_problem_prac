'''
[아이디어]
방법의 수를 찾는 것으로 타일 문제와 비슷하다고 볼 수 있다.
1: 1
2: 1,1 / 2
3: 1,1,1 / 2,1/ 1,2/ 3
4:
    - from 3: 1,1,1,  1/ 2,1  1/1,2  1/ 3  1
    - from 2: 1,1  2 / 2  2
    - from 1: 1  3
이런 식인 것 같음
'''
import sys
input=sys.stdin.readline
T=int(input())
DP=[0]*11 # 0~10까지의 정수를 나타냄
DP[1],DP[2],DP[3]=1,2,4
for i in range(4,11):
    DP[i]=DP[i-1]+DP[i-2]+DP[i-3]
for _ in range(T):
    n=int(input())
    print(DP[n])