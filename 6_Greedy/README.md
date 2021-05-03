# 문제풀이 노트
## lv03-2 단속카메라
### 제출 코드 풀이
```python
def solution(routes):
    routes.sort(key = lambda x: x[0])
    answer = 1
    cam = routes[0][1]
    for r in routes :
        start = r[0]
        end = r[1]
        if start <= cam or end <= cam :
            cam = min(end, cam)
        else :
            answer += 1
            cam = end
    return answer
```
