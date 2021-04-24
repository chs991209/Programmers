# 문제풀이 노트
## lv01 K번째수
### 일반적인 함수에서 반복문 사용하기
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

### map 함수 사용하기
map: Return an **iterator** that applies function to every item of iterable, yielding the results. [출처](https://docs.python.org/3/library/functions.html#map)

map은 iterator를 반환하므로(iter 함수와 비슷한 기능) list 등(next 함수와 비슷한 기능) iterator를 operation 해주는 함수와 함께 사용해야 함
```
>>> def squared(x): 
	return x**2
	
>>> list(map(squared, [1, 2, 3, 4]))
[1, 4, 9, 16]
```

### lambda 함수 사용하기
```
>>> list(map(lambda x: x**2, [1, 2, 3, 4]))
[1, 4, 9, 16]
```
