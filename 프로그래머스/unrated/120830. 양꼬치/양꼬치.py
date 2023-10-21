def solution(n, k):
    k-=(n//10) # 10명마다의 서비스는 가격 지불의 감소요인
    k*=2000
    n*=12000
    answer = n+k
    return answer