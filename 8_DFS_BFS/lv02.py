def dfs(numbers, target, depth) :
    numsum = 0
    if depth < len(numbers) :
        count = count + dfs(numbers, target, depth + 1)
        numbers[depth] = -1 * numbers[depth]
        count = count + dfs(numbers, target, depth + 1)
        return count
    elif depth == len(numbers) :
        if sum(numbers) == target :
            return 1
        return 0

def dfs2(numbers, target, depth, ssum):
    if depth == len(numbers):
        if ssum == target:
            return 1
        return 0
    count = 0
    count += dfs2(numbers, target, depth + 1, ssum + numbers[depth])
    count += dfs2(numbers, target, depth + 1, ssum - numbers[depth])
    return count

def solution(numbers, target) :
    answer = dfs2(numbers, target, 0, 0)
    return answer


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
