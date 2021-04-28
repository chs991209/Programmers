def recursive(numbers, idx) :
    if idx == len(numbers) - 1 :
        return
    numsum = numsum + numbers[idx]
    numsum = numsum - numbers[idx]
    recursive(numbers, idx + 1)

recursive(numbers, 0)

def solution(numbers, target) :
    numsum = []
    for num in numbers :
        numsum.append(-2 * num + sum(numbers))
    return count


print(solution([1, 1, 1, 1, 1], 3))

# still in progress.........
