def solution(n):
    
    if n%2==0:
        n=n
    else:
        n=n-1
    answer = 0
    
    while n!=0:
        answer+=n
        n=n-2
    
    return answer