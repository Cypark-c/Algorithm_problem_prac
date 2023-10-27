N,X=map(int,input().split())
A=list(map(int,input().split(' ')))
if len(A)!=N:
    exit(1)
for elements in A:
    if elements<X:
        print(elements,end=' ')