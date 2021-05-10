## 풍선터트리기
### 코드상세풀이
```python
def solution(a):
    n = len(a)
    left = [0] * n
    right = [0] * n

    small = a[0]
    for i in range(0, n) :
        if a[i] <= small :
            small = a[i]
            left[i] = small
        else :
            left[i] = small

    small = a[-1]
    for i in reversed(range(n)):
        if a[i] <= small :
            small = a[i]
            right[i] = small
        else :
            right[i] = small

    count = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            count += 1
            continue
        if a[i] < left[i-1] or a[i] < right[i+1] :
            count += 1
    return count
```
