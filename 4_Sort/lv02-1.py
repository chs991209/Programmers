def solution(numbers):
    numbers = [str(int) for int in numbers]
    numbers = list(reversed(sorted(numbers, key = lambda x : x*3)))
    numbers = "".join(numbers)
    numbers = int(numbers)
    numbers = str(numbers)
    return numbers
