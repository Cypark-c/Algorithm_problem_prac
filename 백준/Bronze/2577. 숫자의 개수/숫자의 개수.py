A=int(input())
B=int(input())
C=int(input())

X=list(map(int,str(A*B*C)))
# print(X)
backup=[]
for i in range(0,10):
    backup.append(X.count(i))
    print(backup[i])