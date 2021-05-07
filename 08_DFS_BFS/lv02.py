def dfs(numbers, target, depth, numsum):
    count = 0
    if depth < len(numbers):
        count += dfs(numbers, target, depth + 1, numsum + numbers[depth])
        count += dfs(numbers, target, depth + 1, numsum - numbers[depth])
    elif depth == len(numbers):
        if numsum == target:
            return 1
        return 0
    return count

def solution(numbers, target) :
    answer = dfs(numbers, target, 0, 0)
    return answer


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
