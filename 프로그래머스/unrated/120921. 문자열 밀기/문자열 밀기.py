def solution(A, B):
    # 왼쪽으로 미는 케이스 판단은 안해도 되나 봄
    cnt=0 # 미는 횟수 count
    while(A!=B):
        x=A[-1]
        y=A[0:-1]

        A=x+y
        cnt+=1
        
        if cnt==99:
            return -1
        
    return cnt

# 해보니까 큐 넣어서 풀어도 될 것 같긴 한데 시간 복잡도 비교해봐야함.
    
    