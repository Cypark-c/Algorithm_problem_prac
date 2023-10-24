def solution(n): # 재귀함수는 일종의 스택이라고 봐야 함
    x=1 
    answer=1
    while(1):
        answer=answer*x
        
        if answer>n:
            return x-1
    
        x=x+1
    
 