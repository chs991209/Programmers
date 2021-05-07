def solution(array, commands):
    answer = []
    for com in commands :
        i = com[0] - 1
        j = com[1] - 1
        k = com[2] - 1
        arr = array[i:j+1]
        arr = sorted(arr)
        answer.append(arr[k])
    return answer

print("solution1: ", solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


def solution2(array, commands):
    def sort_and_index(com):
        i = com[0] - 1
        j = com[1] - 1
        k = com[2] - 1
        arr = array[i : j + 1]
        arr = sorted(arr)
        return arr[k]
    answer = list(map(sort_and_index, commands))
    return answer

print("solution2: ", solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


def solution3(array, commands):
    return list(map(lambda com: sorted(array[com[0] - 1 : com[1]])[com[2] - 1], commands))

print("solution3: ", solution3([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
