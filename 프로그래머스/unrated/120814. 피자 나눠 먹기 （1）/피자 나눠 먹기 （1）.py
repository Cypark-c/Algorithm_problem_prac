def solution(n):
    '''
    1~7=>1
    8~14=>2
    15~21=>3
    '''
    if n%7!=0:
        return n//7+1
    else:
        return n//7
