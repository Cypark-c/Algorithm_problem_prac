'''
[아이디어]
특정한 경우에 역방향 으로 진행하는게 더 간단.
dp[i]: i 번재 상담 결정시 최대 수익 (뒤부터)
뒤부터 시작하니까 dp[n-1]은 T가 1이 아니라면 0이어야함.
DP에 너무 두들겨 맞는데..
'''

import sys
input=sys.stdin.readline
N=int(input())
# 시간&금액 테이블
t_and_p=[list(map(int,input().split())) for _ in range(N)] # 리스트 사용해서 한번에 맵 오브젝트를 처리
# print(t_and_p)
# 날짜별 최대 금액을 저장할 테이블 선언
DP=[0 for _ in range(N+1)]

for i in range(N-1,-1,-1): # 뒤부터 출발함.
    if i+t_and_p[i][0]<=N:
        DP[i]=max(DP[i+1],DP[i+t_and_p[i][0]]+t_and_p[i][1])
    else:
        DP[i]=DP[i+1]
print(DP[0])