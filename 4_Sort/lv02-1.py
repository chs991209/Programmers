def solution(numbers):
    numbers = [str(int) for int in numbers]

    numbers = list(reversed(sorted(numbers)))
    numbers = "".join(numbers)
    numbers = int(numbers)
    numbers = str(numbers)
    return numbers

print(solution([3, 30, 310, 4]))
