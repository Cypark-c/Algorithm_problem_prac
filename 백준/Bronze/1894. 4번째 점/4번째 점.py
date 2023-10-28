
import sys
for line in sys.stdin:
    '''if line=="\n":
        break'''
    x1,y1,x2,y2,x3,y3,x4,y4=map(float,line.split())

    # 인접한 두 변의 꼭짓점이므로 같은 쌍이 반드시 존재한다.
    points=[]
    points.append([x1,y1])
    points.append([x2,y2])
    points.append([x3,y3])
    points.append([x4,y4]) # 튜플을 넣어줌
    facepoint=[] # 겹치는 꼭지점이자 미지수 포인트와 대각선 관계에 있음
    for idx,point in enumerate(points):
        if points.count(point)>1:
            facepoint=point

    # 이제 중복된 point를 따로 관리하기 위해 제거함
    for i in range(2):
        points.remove(facepoint)

    m=(points[0][0]+points[1][0])/2
    n= (points[0][1] + points[1][1])/2
    # print(m,n,facepoint)
    p=2*m-facepoint[0]
    q = 2 * n -facepoint[1]
    print(f'{p:.3f}',f'{q:.3f}')