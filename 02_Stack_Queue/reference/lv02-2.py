# Brute Force

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:       # 하락했을시
                answer[i] = answer[i] + 1
                break
            else:
                answer[i] = answer[i] + 1
    return answer

# Stack

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        i = prices.popleft()
        count = 0
        for j in prices:
            if j < i:               # 하락했을시
                count = count + 1
                break
            else:
                count = count + 1
        answer.append(count)
    return answer
