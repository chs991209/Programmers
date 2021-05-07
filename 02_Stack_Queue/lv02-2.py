def solution(prices):
    answer = [i for i in reversed(range(len(prices)))]
    time = [0] * len(prices)
    for i in range(len(prices) - 1) :
        for j in range(i + 1, len(prices)) :
            if prices[j] < prices[i] :
                time[i] = time[i] + 1
    for i in ranege(len(prices)) :
        answer[i] = answer[i] - time[i]
    return answer

# Still in progress... 2 out of 3
