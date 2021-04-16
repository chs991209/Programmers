def solution(participant, completion):
    for p in participant:
        flag = 0
        for c in completion:
            if p == c:
                flag = 1
                completion.remove(c)
                break
        if not flag:
            return p
