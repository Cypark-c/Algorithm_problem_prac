import sys
input=sys.stdin.readline
ind_list1=[0,2,4,6] # 하얀 (0,2,4,6 행)
ind_list2=[1,3,5,7] # 하얀 (1,3,5,7 행)
cnt=0
for i in range(8):
    line=list(input().rstrip()) # line 입력받기
    if i%2==0:
        ind_list=ind_list1
    else:
        ind_list=ind_list2
    for ind in ind_list:
        if line[ind]=='F':
            cnt+=1
print(cnt)