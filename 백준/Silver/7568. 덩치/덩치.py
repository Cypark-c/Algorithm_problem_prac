import sys
input=sys.stdin.readline
N=int(input())
st_list=[]

for _ in range(N):
    st_list.append(tuple(map(int,input().split())))

'''
일단은 덩치에서 비교 우위를 가지려면 둘 모두 이겨야함.
그 비교 우위만큼 카운팅 하면 될 것 같은데
'''

cnt_list=[] # 비교 강도를 체크하기 위한 리스트

for i in range(N):
    cnt=0
    for j in range(N):
        if j!=i:
            if (st_list[i][0]<st_list[j][0]) and (st_list[i][1]<st_list[j][1]):
                cnt+=1
    cnt_list.append(cnt)

for i in range(N):
    cnt_list[i]+=1
    print(cnt_list[i],end=' ')