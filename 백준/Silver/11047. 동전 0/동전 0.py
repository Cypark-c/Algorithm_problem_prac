# 동전을 적절히 사용해서 그 가치의 합을 K로 만든다
N,K=map(int,input().split())
# 동전 입력 받기
coinlist=[]
for i in range(N):
    coinlist.append(int(input()))

cnt=0

for i in range(N-1,-1,-1): # 코인을 역순으로 찾아가며 비교함
    if coinlist[i]<=K:
        cnt+=K//coinlist[i]
        K=K-(K//coinlist[i])*coinlist[i]


print(cnt)