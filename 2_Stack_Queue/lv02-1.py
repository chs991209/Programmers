def solution(bridge_length, weight, truck_weights):
    answer = bridge_length * len(truck_weights) + 1
    i = 1
    truck_bridge = truck_weights[0]
    for i in range(len(truck_weights)) :
        if truck_bridge > weight :
            i = i + 1
        else :
            truck_bridge = truck_bridge + truck_weights[i]
            answer = answer - 1
            if truck_bridge > weight :
                break
            i = i + 1
            
    return answer

# still in progress.. 1 out of 3
