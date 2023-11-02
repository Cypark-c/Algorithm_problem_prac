import sys
input=sys.stdin.readline
Par_set={'(',')'}
T=int(input())
stack=[]
for _ in range(T):
    stack=list(map(str,input().rstrip()))
    #print(stack)
    left_cnt=0
    right_cnt=0
    while(len(stack)!=0):
        p=stack.pop()
        if p==')':
            right_cnt+=1
        else:
            left_cnt+=1

        if left_cnt>right_cnt:
            print("NO")
            break

        if (len(stack)==0):
            if (right_cnt==left_cnt):
                print("YES")
            else:
                print("NO")
