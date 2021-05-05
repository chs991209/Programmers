def solution(number, k):
    number = list(map(int, number))
    number.sort()
    number = number[k:len(number) + 1]
    return number

number = "1924"
k = 2
print(solution(number, k))
