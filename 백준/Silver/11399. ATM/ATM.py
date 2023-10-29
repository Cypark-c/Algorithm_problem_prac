'''
P1=3, P2=1, P3=4, P4=3 P5=2
[P1,P2,P3,P4,P5]
1번은 3분만에
2번은 3+1분 즉 4분
3번은 8분만에..

[P2=1,P5=2,P1=3,P4=3,P3=4]
2번은 1분
5번은 1+2=3분
1번은 1+2+3=6분
4번은  9분
3번은 13분
모두 합하면 1+3+6+9+13=32
'''
# 예시만 보더라도, 그냥 time이 작은 순서대로 가야 그렇게 배열을 만들어야 함

N=int(input())
X=list(map(int,input().split(' ')))
X.sort()
sum_tot=0
for i in range(N):
    part_sum=0
    part_sum=sum(X[:i+1])
    sum_tot+=part_sum
print(sum_tot)