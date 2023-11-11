'''
[아이디어]
재귀로 풀면 시간초과일 것이 분명
'''
n=int(input())

def fibo_dyna(n):
    DP=[0 for _ in range(n+1)] #index: 0~n
    DP[1]=1 # 이거 좀 주의해야함.. DP[2]=1로 해버리면 좀 위험함 인덱스가 존재하지 않는데 존재하지 않는 것처럼 서술한 셈임

    if n<2:
        return 1
    else:
        for i in range(2,n+1):
            DP[i]=DP[i-1]+DP[i-2]
        return DP[n]

print(fibo_dyna(n))