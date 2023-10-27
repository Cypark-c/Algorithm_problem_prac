N,K=map(int,input().split())

K_list=[]

for i in range(1,N+1):
    if N%i==0:
        K_list.append(i)

if len(K_list)<K:
    print(0)
else:
    print(K_list[K-1])