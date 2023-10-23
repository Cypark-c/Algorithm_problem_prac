def solution(picture, k):
    # 일단은 리스트 원소의 각 글자마다 k번 반복해야한다.
    answer=[]
    
    for i in range(len(picture)):
        str=''
        
        for j in range(len(picture[i])): 
            str=str+picture[i][j]*k
        
        for i in range(0,k):
            answer.append(str)
            
    return answer
