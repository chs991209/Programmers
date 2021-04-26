# 문제풀이 노트
## lv01 K번째수
### 1. 일반적인 함수에서 반복문 사용하기
for문을 이용한다
```
>>> def squared(num_list):
	result = []
	for num in num_list:
		result.append(num**2)
	return result

>>> result = squared([1, 2, 3, 4])
>>> result
[1, 4, 9, 16]
```

### 2. map 함수 사용하기
map: Return an **iterator** that applies function to every item of iterable, yielding the results. [출처](https://docs.python.org/3/library/functions.html#map)

map은(iter 함수와 비슷한 기능) iterator를 반환하므로 list 등(next 함수와 비슷한 기능) iterator를 operation 해주는 함수와 함께 사용해야 함
```
>>> def squared(x): 
	return x**2
	
>>> list(map(squared, [1, 2, 3, 4]))
[1, 4, 9, 16]
```

### 3. lambda 함수 사용하기
```
>>> list(map(lambda x: x**2, [1, 2, 3, 4]))
[1, 4, 9, 16]
```

## lv02-1 가장 큰 수
### 숫자 정렬 vs. 문자열 정렬
숫자로 이루어진 리스트를 정렬하면 결과는 값을 오름차순으로 보여준다.

문자열로 이루어진 리스트를 정렬하면 그 결과는 값 자체가 아니라 가장 큰 자릿수 기준으로 오름차순이다.

- 숫자 정렬 시
```
>>> num_list = [9, 111, 22, 3]
>>> num_list = sorted(num_list)
>>> num_list
[3, 9, 22, 111]
```
- 문자열 정렬 시
```
>>> str_list = ["9", "111", "22", "3"]
>>> str_list = sorted(str_list)
>>> str_list
['111', '22', '3', '9']
```

### 숫자 리스트를 문자 리스트로 변환하기
- for문 이용하기
```
>>> list_intt = [1, 2, 3, 4]
>>> list_strring = [str(intt) for intt in list_intt]
>>> list_strring
['1', '2', '3', '4']
```
- map 이용하기
```
>>> list_int = [1, 2, 3]
>>> list_string = map(str, list_int)
>>> print(list(list_string))
['1', '2', '3']
```

### 제출 코드 상세 풀이
```
def solution(numbers):
    numbers = [str(int) for int in numbers]				# convert int to str
    numbers = list(reversed(sorted(numbers, key = lambda x : x*3)))	# repeat str 3 times(bc numbers <= 1,000) and use it as a key to sort
    numbers = "".join(numbers)						# make list into a string
    numbers = int(numbers)						# in order to deal with "000", which supposed to be 0
    numbers = str(numbers)						# condition: return form in string
    return numbers
```
