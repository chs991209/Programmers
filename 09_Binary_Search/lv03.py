n = 6
times = [7, 10]

def solution(n, times):
    answer = min(max(7 * 1, 10 * (n-1)), max(7 * 2, 10 * (n-2)),
                 max(7 * 3, 10 * (n-3)), max(7 * 4, 10 * (n-4)),
                 max(7 * 5, 10 * (n-5)), max(7 * 6, 10 * (n-6)))
    print(answer)

solution(n, times)
