def solution(n, works):
    works = list(reversed(sorted(works)))
    i = 0
    j = n
    answer = 0
    while j > 0 :
        if works[i] > 0 :
        	works[i] = works[i] - 1
        works = list(reversed(sorted(works)))
        j -= 1
    i = 0
    k = len(works)
    while k - i > 0 :
        answer += works[i] * works[i]
        i += 1
    return answer
