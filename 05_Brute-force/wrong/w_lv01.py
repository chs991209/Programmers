answers = [2, 1, 2, 3, 2, 4, 2, 5]
students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
for i in range(len(students)) :
    win = 0
    for j in range(len(answers)) :
        n = len(students[i])
        if (answers[j] == students[i][j%n]) :
            win += 1
    students.append(win)
winner = [students[3], students[4], students[5]]
answer = winner.index(max(winner)) + 1          # only returns 1 answer(cannot get several indices of max values)
print(answer)
