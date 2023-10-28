def factorial(K):
    if K==0:
        return 1
    else:
        return K*factorial(K-1)

T=int(input()) # test case
for _ in range(T):
    N,M=map(int,input().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))