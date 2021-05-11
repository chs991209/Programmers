## 풍선터트리기 [**문제보기**](https://programmers.co.kr/learn/courses/30/lessons/68646)
### 접근법
- dynamic programming(DP, 동적계획법)
- 인접한 풍선을 비교해서 터트리므로 어떠한 풍선의 왼쪽과 오른쪽을 비교해야 함
- 작은 풍선은 최대 한 번 터트릴 수 있으므로, 일단 큰 풍선을 먼저 터트린다고 가정
- 어떠한 풍선의 왼쪽에서 가장 작은 수를 가진 풍선을 남기고 오른쪽에서도 가장 작은 수를 가진 풍선을 남기고 나머지는 터트림
- 어떠한 풍선은 남은 세 풍선 중 가장 크지만 않으면 끝까지 남을 수 있음
- 즉, 어떠한 풍선이 끝까지 남을 수 있는 조건은: **풍선 < 왼** or **풍선 < 오른**
### 내림차순 반복문
- reversed(range(end, start+1)) 이용: range의 순서만 바꾼것
```python
>>> for i in range(0, 3) :
...     print(i)
...
0
1
2
```
```python
>>> for i in reversed(range(0, 3)) :
...     print(i)
...
2
1
0
```
- range(start, end-1, -1) 이용: 시작과 끝을 잘 고려해야 함
```python
>>> for i in range(2, -1, -1) :
...     print(i)
...
2
1
0
```
### 코드상세풀이
```python
def solution(a):
    n = len(a)
    left = [0] * n              # 왼쪽에서 가장 작은 수 저장하기 위한 리스트
    right = [0] * n             # 오른쪽에서 가장 작은 수 저장하기 위한 리스트

    small = a[0]                # 왼쪽에서 가장 작은 수 찾는 시작지점
    for i in range(0, n) :
        if a[i] <= small :
            small = a[i]
            left[i] = small
        else :
            left[i] = small

    small = a[-1]               # 오른쪽에서 가장 작은 수 찾는 시작지점
    for i in reversed(range(n)):
        if a[i] <= small :
            small = a[i]
            right[i] = small
        else :
            right[i] = small

    count = 0
    for i in range(n):
        if i == 0 or i == n - 1:    # 가장 왼쪽이나 가장 오른쪽에 있는 풍선이라면
            count += 1              # 항상 끝까지 남을 수 있음(큰 것만 터트리다가 마지막에 작든 크든 그 풍선만 남기기)
            continue
        if a[i] < left[i-1] or a[i] < right[i+1] :  # 풍선이 끝까지 남을 수 있는 조건
            count += 1
    return count
```
