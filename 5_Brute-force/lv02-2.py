def solution(brown, yellow):
    for m in range(brown // 2, 3, -1) :
        for n in range(3, m + 1) :
            if (m * n == brown + yellow) :
               if ((m - 2) * (n - 2) == yellow) :
               #if (m * n - (m - 2)*(n - 2) == brown) :
               #if ((m + n) * 2 - 4 == brown):
                    return [m, n]

print(solution(brown, yellow))
