# lv01 모의고사
## max()
max() 함수는 최댓값을 돌려준다.
```
>>> max([1, 2, 3])
3
```


## max value 대신 max value를 갖는 index 구하기
index(max()) 함수를 사용하면 된다.
```
>>> a_list = [1, 2, 3]
>>> max_index = a_list.index(max(a_list))
>>> max_index
	2
```


## multiple indices of max values 구하기
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
