def solution(answers):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(students)) :
        win = 0
        for j in range(len(answers)) :
            if (answers[j] == students[i][j%len(students[i])]) :
                win += 1
        students.append(win)

    winner = [students[3], students[4], students[5]]
    max_value = max(winner)
    indices = [index + 1 for index, value in enumerate(winner) if value == max_value]
    return(indices)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
