# 문제풀이 노트
## lv01 체육복
### 유의할 점
- 반복문 실행 시, 반복할 대상을 수정(추가하거나 제거)하면 안 됨 -> index 순서대로 접근하기 때문.
- 파이썬에서 리스트 간의 뺄셈은 지원하지 않음. 대신 집합 간의 뺄셈은 가능. set() 이용하기.
### 리스트 간의 뺄셈 구현하기
- 한 번에 빼기
```
>>> A = [1, 2, 3, 4]
>>> B = [3, 4, 5, 6]
>>> A, B = list(set(A) - set(B)), list(set(B) - set(A))
>>> A
[1, 2]
>>> B
[5, 6]
```
- 새로운 리스트 만든 후 빼기
```
>>> A = [1, 2, 3, 4]
>>> B = [3, 4, 5, 6]
>>> C = []
>>> for a in A :
...     if a in B :
...             C.append(a)
...
>>> C
[3, 4]
>>> A = list(set(A) - set(C))
>>> B = list(set(B) - set(C))
>>> A
[1, 2]
>>> B
[5, 6]
```
### 제출 코드 풀이
```python
def solution(n, lost, reserve):
    nums = 0
    same = []
    student = n - len(lost)                     # student에서 잃어버린 개수를 모두 뺀다(최소치를 구한다)
    
    for l in lost :                             # 도난 당했으나, 본인의 여벌 체육복이 있는 경우를 먼저 고려해야 한다.
        if l in reserve :
            same.append(l)                      # lost[] == reserve[] 인 요소를 찾아 same[]에 담는다
    student += len(same)                        # same[] 개수만큼 더해준다(도난 당했으나, 여벌 있는 경우)
    lost = list(set(lost) - set(same))
    reserve = list(set(reserve) - set(same))
    
    for l in lost :
        if l - 1 in reserve:
            reserve.remove(l - 1)       # lost에 대한 반복문 실행 중이므로, lost리스트의 요소는 건드리지 않아야 함
            nums += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            nums += 1
    student = student + nums
    return student
```
## lv03-2 단속카메라
### 제출 코드 풀이
```python
def solution(routes):
    routes.sort(key = lambda x: x[0])    # 진입이 빠른 순서로 정렬
    answer = 1
    cam = routes[0][1]
    for r in routes :
        start = r[0]
        end = r[1]
                                         # 알고리즘 설명: 그룹 정하기 -> 그 중에 가장 빠른 진출 시점을 골라 -> cam 설치 -> 다음 그룹                                         
        if start <= cam or end <= cam :  # 그룹 정하기(진입 기준 정렬되어 있으므로 'start는 cam 보다 앞에 있지만 end는 뒤에 있는 경우 - 즉, 진입은 앞 그룹에 & 진출은 뒷 그룹에 "끼인 경우"도 포함됨, 아래 그림에서 for문 2번 경우)
            cam = min(end, cam)          # 가장 빠른 진출 시점(==최소 end) 찾기

        else :                           # 한 그룹이 끝났고, 다음 그룹으로 넘어감
            answer += 1                  # 한 그룹 끝날 때 카메라 설치
            cam = end                    # cam위치는 다음 그룹 시작할 때의 end위치로 옮겨둠(이렇게 해야 그 그룹의 모든 end에 대해 min값 찾기 가능)
            
    return answer
```
### 진입 기준 sort 후 for문 실행순서 
![참조](https://github.com/euiminnn/image-upload/blob/master/cam.png)
