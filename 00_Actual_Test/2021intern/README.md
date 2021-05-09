## 문제1번: 영단어를 숫자로 변환

### 코드 상세 풀이
```python
def solution(s):
    answer = []
    i = 0
    while i < len(s) :		# 반복문 실행 시 전체를 순서대로 반복하는게  아니라 index를 조정할 때에는 for문보다 while문이 더욱 적합함
        if s[i] == 'z':			                # s = "zero" 인 경우
            answer.append(0)
            i += 4				                # z에 있던 index를 4번 옮겨 다음 단어(혹은 숫자) 탐색
        elif s[i] == 'o':
            answer.append(1)
            i += 3
        elif s[i] == 't' and s[i+1] == 'w':		# s = "two"인 경우, three와 구별하기 위해 두번째 자리까지 일치하는지 검사
            answer.append(2)
            i += 3                              # t에 있던 index를 3번 옮겨 다음 단어(혹은 숫자) 탐색
        elif s[i] == 't' and s[i+1] == 'h':
            answer.append(3)
            i += 5
        elif s[i] == 'f' and s[i+1] == 'o':
            answer.append(4)
            i += 4
        elif s[i] == 'f' and s[i+1] == 'i':
            answer.append(5)
            i += 4
        elif s[i] == 's' and s[i+1] == 'i':
            answer.append(6)
            i += 3
        elif s[i] == 's' and s[i+1] == 'e':
            answer.append(7)
            i += 5
        elif s[i] == 'e' :
            answer.append(8)
            i += 5
        elif s[i] == 'n' :
            answer.append(9)
            i += 4
        elif '0' <= s[i] <= '9' :
            answer.append(s[i])
            i += 1
    answer = [str(int) for int in answer]		# answer은 숫자는 str로, 영단어는 숫자로 들어오게 된다. 이 중 str을 모두 int로 바꾸기
    answer = "".join(answer)
    answer = int(answer)
    return answer
```
