# 문제풀이 노트
## lv01 모의고사
### max()
max() 함수는 최댓값을 돌려준다.
```
>>> max([1, 2, 3])
3
```


### max value 대신 max value를 갖는 index 구하기
index(max()) 함수를 사용하면 된다.
```
>>> a_list = [1, 2, 3]
>>> max_index = a_list.index(max(a_list))
>>> max_index
2
```


### multiple indices of max values 구하기
최댓값이 여러개일 경우 그 모든 index를 구하기

max value를 구한 후, max value를 갖는 모든 index를 구하면 된다.

index값을 함께 리턴해주는 enumerate를 이용했다.
```
>>> a_list = [1, 3, 2, 3]
>>> max_value = max(a_list)
>>> indices = [index for index, value in enumerate(a_list) if value == max_value]
>>> indices
[1, 3]
```

## lv02-2 카펫
### 내림차순 정렬
```
>>> a_list = [2, 3, 1, 4]
>>> sorted(a_list, reverse = True)
[4, 3, 2, 1]
```

### 큰 값 부터 for문 실행하기(range, max, min, -1)
```
>>> for i in range(3, 0, -1) :
	print(i, end = "")
321
```

### 큰 값 부터 for문 실행하기(reversed(range()))
```
>>> for i in reversed(range(0, 3)) :
	print(i, end = "")
210
```

### 사각형 만들어지는지 확인하기
```
>>> if ((m - 2) * (n - 2) == yellow) :
	return answer
```
또는
```
>>> if (m * n - (m - 2)*(n - 2) == brown) :
	return answer
```
또는
```
>>> if ((m + n) * 2 - 4 == brown) :
	return answer
```
