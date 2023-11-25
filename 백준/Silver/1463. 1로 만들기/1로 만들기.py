'''
아 그냥 좀 짜증남.
DP를 한번 복습하는게 좋을 것 같다.
'''
N=int(input())
dp=[0]*(N+1)
for i in range(2,N+1):
    dp[i]=dp[i-1]+1
    if not i%2:
        dp[i]=min(dp[i],dp[i//2]+1)
    if not i%3:
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[N])