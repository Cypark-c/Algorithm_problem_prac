A,B=map(int,input().split())
C=int(input())
A+=(B+C)//60
A=A%24
B=B+C-((B+C)//60)*60
print(A,B)
