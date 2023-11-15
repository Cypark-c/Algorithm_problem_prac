import sys
input=sys.stdin.readline
mat=[]
result=[]
for i in range(9):
    mat.append(list(map(int,input().split())))
    m_value=max(mat[i])
    j=mat[i].index(m_value)
    result.append([i,j,m_value])

u=max(result,key=lambda x: x[2])
print(u[2])
print(u[0]+1,u[1]+1)
# 뭔가 안깔끔한데 ㅡㅡ