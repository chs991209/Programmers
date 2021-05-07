def dfs(n, computers, v, visited) :
    visited[v] = True
    for j in range(n) :
        if j != v and computers[v][j] == 1 :
            if visited[j] == False :
                dfs(n, computers, j, visited)

def solution(n, computers) :
    count = 0
    visited = [False] * n
    for i in range(n) :
        if visited[i] == False :
            dfs(n, computers, i, visited)
            count += 1
    return count


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 RESULT                              "
"                              great job :)                           "
"                                                                     "
"                               logic: OK(100)                        "
"                                time: OK                             "
"                                                                     "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
