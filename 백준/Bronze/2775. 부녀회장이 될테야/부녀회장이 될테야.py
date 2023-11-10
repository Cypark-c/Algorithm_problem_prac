'''
일단 기본적 문제로는 괜찮은것 같다.

[아이디어]
a층의 b호? a-1층 1~b호 사람들의 수의 합만큼 사람들을 데려온다.
대략 [a][b]: [a-1][1]+[a-1][2]+[a-1][3]+...+[a-1][b] 이런 아이디어를 짤 수 있음
아파트는 0층도 있고, 각 층엔 1호부터 있음
0층이라면 1호엔 1명, 2호엔 2명...n호엔 n명

[변수]
k층 n호, 테스트 케이스 T
'''

import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())

    # 문제의 실행시간이 0.5초에 불과하므로 DP 기법을 써야한다.
    mans=[[0]*(n+1) for _ in range(k+1)] # 0호를 넣어도 크게 상관 없다.
    mans[0]=[i for i in range(n+1)] # 0,1,2,...,n, 0층의 정보
    if k>0: # 0층보다 위에서 거주할 경우
        for i in range(1,k+1):
            for j in range(1,n+1):
                if j==1:
                    mans[i][j]=1
                else: # j>2
                    mans[i][j]=mans[i-1][j]+mans[i][j-1]
    print(mans[k][n])