X=[]
idx=0
for i in range(9):
    value=int(input())
    X.append(value)
    if i==0:
        max_X=X[0]
        idx=0
    if value>max_X:
        max_X=value
        idx=i
print(max_X)
print(idx+1) # 배열 인덱스는 0부터 시작하니 그 부분에 주의