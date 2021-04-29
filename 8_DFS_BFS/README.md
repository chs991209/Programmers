# DFS & BFS
<p align = "center"><img src = "https://github.com/euiminnn/py-practice/blob/master/dfs.png" width = "600"></p>

```python
# graph[n]은 n번째 노드에 연결된 정보
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]
```


## 탐색 순서
- DFS는 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5
- BFS는 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6


## DFS 코드
```python
def dfs(graph, v, visited) :
	visited[v] = True
	print(v, end=' ')
	for i in graph[v] :
		if not visited[i] :
			dfs(graph, i, visited)

visited = [False] * 9

dfs(graph, 1, visited)
```


## BFS 코드
```python
from collections import deque

def bfs(graph, start, visited) :
	queue = deque([start])
	visited[start] = True
	while queue :
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v] :
			if not visited[i] :
				queue.append(i)
				visited[i] = True

visited = [False] * 9

bfs(graph, 1, visited)
```

# 문제풀이 노트
## lv02 타겟넘버


## lv03-2 네트워크
### 제출 코드 풀이
```python
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
```
