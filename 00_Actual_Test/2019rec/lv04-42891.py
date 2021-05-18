def solution(food_times, k):
    #arr = sorted([(food_times[i], i+1) for i in range(0, len(food_times))], key=lambda x : x[0])
    t = 0
    answer = 0
    while True :
        for i in range(0, len(food_times)) :
            if food_times[i] > 0 :
                food_times[i] -= 1
                t += 1
                if t == k :
                    return i + 1
            else :
                continue

food_times = [2, 1, 2]
k = 5
print(solution(food_times, k))
