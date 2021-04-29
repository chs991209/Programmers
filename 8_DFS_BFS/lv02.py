def dfs(numbers, target, depth) :
    count = 0
    if depth < len(numbers) :
        count = count + dfs(numbers, target, depth + 1)
        numbers[depth] = -1 * numbers[depth]
        count = count + dfs(numbers, target, depth + 1)
        return count
    elif depth == len(numbers) :
        if sum(numbers) == target :
            return 1
        return 0


def solution(numbers, target) :
    answer = dfs(numbers, target, 0)
    return answer


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
