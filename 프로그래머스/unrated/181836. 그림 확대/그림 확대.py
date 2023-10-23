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

# 아래와 같은 풀이도 있음

'''
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer
'''

'''
확실히 replace를 사용했다면, 조금 더 쉽게 풀 수 있었을텐데.. 많이 활용을 해보지 않아서 바로 생각이 나지 않았다.
