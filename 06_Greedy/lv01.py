def solution(n, lost, reserve):
    nums = 0
    same = []
    student = n - len(lost)
    for l in lost :
        if l in reserve :
            same.append(l)
    student += len(same)
    lost = list(set(lost) - set(same))
    reserve = list(set(reserve) - set(same))
    lost = sorted(lost)
    for l in lost :
        if l - 1 in reserve:
            reserve.remove(l - 1)
            nums += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            nums += 1
    student = student + nums
    return student
