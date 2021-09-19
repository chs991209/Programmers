def solution(participant, completion):
    part = participant
    for p in part :
        for c in completion :
            if p == c :
                participant.remove(c)
    return participant

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))


# 왜 결과가 ['josipa', 'vinko']가 나오지?
