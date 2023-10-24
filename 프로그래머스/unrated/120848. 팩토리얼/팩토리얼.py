def solution(n): # 단순 반복문 사용
    x=1 
    answer=1
    while(1):
        answer=answer*x
        
        if answer>n:
            return x-1
    
        x=x+1
    
 