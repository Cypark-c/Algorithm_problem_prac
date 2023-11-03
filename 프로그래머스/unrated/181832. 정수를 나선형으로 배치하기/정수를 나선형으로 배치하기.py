# 일단은 이렇게 풀면 안된다.
def circulation(vector, fill, matrix, x_pos, y_pos, n):
    if n==1:
        matrix[x_pos][y_pos]=1
        return
    if vector == [0, 1]:  # 동쪽
        for _ in range(n):  # 동쪽으로 진행
            if (matrix[x_pos][y_pos] != 0) or y_pos == n - 1:

                if matrix[x_pos][y_pos] != 0:

                    circulation([1, 0], fill, matrix, x_pos+1, y_pos-1, n)
                    return
                circulation([1, 0], fill, matrix, x_pos, y_pos, n)  # 남쪽으로 진행필요

                return
            matrix[x_pos][y_pos] = fill

            if fill == n * n:
                return
            y_pos += 1
            fill += 1

    elif vector == [1, 0]:  # 남쪽
        for _ in range(n):  # 남쪽으로 진행
            if (matrix[x_pos][y_pos] != 0) or x_pos == n - 1:

                if matrix[x_pos][y_pos] != 0:

                    circulation([0, -1], fill, matrix, x_pos-1, y_pos-1, n)
                    return
                circulation([0, -1], fill, matrix, x_pos, y_pos, n)  # 서쪽으로 진행필요

                return
            matrix[x_pos][y_pos] = fill


            if fill == n * n:
                return
            x_pos += 1
            fill += 1

    elif vector == [0, -1]: #서쪽
        for _ in range(n):  # 서쪽으로 진행
            if matrix[x_pos][y_pos] != 0 or y_pos == 0:

                if matrix[x_pos][y_pos] != 0:

                    circulation([-1, 0], fill, matrix, x_pos-1, y_pos + 1, n)
                    return
                circulation([-1, 0], fill, matrix, x_pos, y_pos, n)

                return
            matrix[x_pos][y_pos] = fill

            if fill == n * n:
                return
            y_pos -= 1
            fill += 1
    else:  # vector==[-1,0]
        for _ in range(n):  # 북쪽으로 진행
            if matrix[x_pos][y_pos] != 0 or x_pos == 0:

                if matrix[x_pos][y_pos] != 0:

                    circulation([0, 1], fill, matrix, x_pos+1, y_pos + 1, n)
                    return
                circulation([0, 1], fill, matrix, x_pos+1, y_pos, n)

                return
            matrix[x_pos][y_pos] = fill

            if fill == n * n:
                return
            x_pos -= 1
            fill += 1


def solution(n):
    '''
    # 나선형 배열...how?
    초기위치를 (0,0)으로 잡고 순회하면서 채워야 할듯
    (0,0)->(0,n-1)
    (0,n-1)->(n-1,n-1)
    (n-1,n-1)->(n-1,0)
    (n-1,0)->(1,0) : 1 cycle
    (1,0)->(1,n-2) .... 이 사이클만 잘 짜면 될 것 같은데
    '''
    matrix = [[0] * n for _ in range(n)]

    circulation([0, 1], 1, matrix, 0, 0, n)
    
    return matrix
