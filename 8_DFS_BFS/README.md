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
    visited[v] = True						# 방문 체크하기
    for j in range(n) :
        if j != v and computers[v][j] == 1 :			# 자기 자신이 아니고 and 이어진 네트워크라면
            if visited[j] == False :				# 방문 전이라면
                dfs(n, computers, j, visited)			# dfs 탐색 이어나감

def solution(n, computers) :
    count = 0
    visited = [False] * n					# 방문 출석부 만들기
    for i in range(n) :
        if visited[i] == False :				# 방문 전이라면
            dfs(n, computers, i, visited)			# dfs 탐색 시작
            count += 1						# 새로 시작할 때 마다 count+1(이어지지 않은 네트워크 수 세기)
    return count
```
