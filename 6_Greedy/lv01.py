def solution(n, lost, reserve):
    nums = 0
    _min = n - len(lost)
    for l in lost :
        if l in reserve:
            reserve.remove(l)
            nums += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            nums += 1
        elif l - 1 in reserve:
            reserve.remove(l - 1)
            nums += 1
    _min = _min + nums
    return _min
