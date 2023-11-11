'''
[아이디어]
H를 행, W를 열로 둘 수가 있을 것. H랑 W가 1부터 시작함
모든 구름은 동쪽으로만 이동, 외부에서 구름이 추가되는 경우는 없음
즉 초기에 구름은 지도로서 주어지고 그 후에 구름은 1분뒤에 (i,j)에서 j만 바뀜.
현재 구름이 있다면 0분후에 오는 것이다라고 설정
하나 더 생각해봐야 할 것은, 한 지점을 구름이 여러번 거쳐갈 수 있는데 이 때는
처음 도달한 시간만 인정해야한다.

위의 아이디어대로 접근을 했는데 생각외로 시간이 걸려버림. 뭐가 부족했는지 확실히 짚고 가자.
'''

import sys
input=sys.stdin.readline
H,W=map(int,input().split())

# 구름맵 초기화.. 그런데 초기화와 동시에 한번에 처리할 수 있을 듯 함
Map_cloud=[]
Map_cloud_print=[[-1]*W for _ in range(H)] # -1로 초기화
for i in range(H):
    Map_cloud.append(input().rstrip())
    # print(Map_cloud[i]) # for debugging

    # 각 행마다 c가 들어있는 인덱스를 찾아야 함. 그런데 있을때나 찾을 수 있음
    # 그리고 c는 여러개 있을 수 있다.
    cloud_index=[]
    if Map_cloud[i].count('c')!=0:
        for j in range(0,W):
            if Map_cloud[i][j]=='c':
                cloud_index.append(j)

    # cloud_index에 들어있는 인덱스 기준으로 라인 처리 완료하면 된다.
    # [처리1] 0과 -1에 대한 처리
    if cloud_index!=[]: # 뭔가 구름이 있다고 할 때 처리해야함
        for k in range(0,W):
            if cloud_index.count(k)!=0:
                Map_cloud_print[i][k]=0
            else:
                Map_cloud_print[i][k]=-1
    else:
        for k in range(0, W):
            Map_cloud_print[i][k] = -1
    # [처리2] 1,2,3 등의 구름의 이동에 관한 처리
    # 순회하면서 보면 될 것 같음
    minute=-1
    for s in range(0,W):
        if (minute>0) and Map_cloud_print[i][s]!=0:
            Map_cloud_print[i][s]=minute # minute를 넣어준다,
            minute+=1 # 구름이 있다면 다음칸에도 들어가게 된다.

        if Map_cloud_print[i][s]==0: # 구름을 만났으니 minute 초기화
            minute=1 # 이제 구름을 만나서 카운팅 하기 시작할 것

    for q in range(W):
        print(Map_cloud_print[i][q],end=' ')
    print("")