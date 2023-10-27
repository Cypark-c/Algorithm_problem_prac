# 생각보다 참고할 내용이 있는 문제인듯하다.
remlist=[-1 for i in range(42)] # 나올 수 있는 총 나머지 0~41임 일단 -1로 초기화
cnt=0
for _ in range(10):
    A=int(input())
    if (A%42>-1)&(remlist[A%42]!=A%42):
        remlist[A%42]=A%42
        cnt+=1

print(cnt)