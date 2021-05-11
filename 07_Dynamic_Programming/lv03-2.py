def solution(triangle) :
    n = len(triangle)
    answer = []
    a = sum(triangle[0])
    for t in triangle[1] :
        i = triangle[1].index(t)
        a += t
        #print("t = ", t)
        for j in range(2, n) :
            m = max(triangle[j][i], triangle[j][i+1])
            #print("m = ", m)
            i = triangle[j].index(m)
            a += m
        answer.append(a)
        a = sum(triangle[0])
    return max(answer)
"""

    m = max(triangle[1])
    i = triangle[1].index(m)    #enum쓰기
    a += m
    m = max(triangle[2][i], triangle[2][i+1])
    i = triangle[2].index(m)
    a += m
    m = max(triangle[3][i], triangle[3][i+1])
    i = triangle[3].index(m)
    a += m
    m = max(triangle[4][i], triangle[4][i+1])
    i = triangle[4].index(m)
    a += m
"""
    
    #return max(answer)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
