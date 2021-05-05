def solution(n, lost, reserve):
    student = [1 for _ in range(n)]
    for r in reserve :
        student[r - 1] += 1
    for l in lost:
        student[l - 1] -= 1
    for i in range(n - 1):
        if student[i] == 0 and student[i + 1] == 2:
            student[i] = 1
            student[i + 1] = 1
    for i in range(1, n):
        if student[i] == 0 and student[i - 1] == 2:
            student[i] = 1
            student[i - 1] = 1
    return sum(list(map(lambda x : x > 0, student)))
