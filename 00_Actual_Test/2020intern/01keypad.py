def convertto(num) :
    answer = "error"
    if num == 1 :
        answer = [0, 0]
    elif num == 2 :
        answer = [0, 1]
    elif num == 3 :
        answer = [0, 2]
    elif num == 4 :
        answer = [1, 0]
    elif num == 5 :
        answer = [1, 1]
    elif num == 6 :
        answer = [1, 2]
    elif num == 7 :
        answer = [2, 0]
    elif num == 8 :
        answer = [2, 1]
    elif num == 9 :
        answer = [2, 2]
    elif num == '*' :
        answer = [3, 0]
    elif num == 0 :
        answer = [3, 1]
    elif num == '#' :
        answer = [3, 2]
    return answer

def solution(numbers, hand):
    answer = [0] * len(numbers)
    hand_l = '*'
    hand_r = '#'
    for i in range(0, len(numbers)) :
        if numbers[i] in [1, 4, 7] :
            answer[i] = 'L'
            hand_l = numbers[i]
        elif numbers[i] in [3, 6, 9] :
            answer[i] = 'R'
            hand_r = numbers[i]
        else :
            numbers_pos = list(map(convertto, numbers))[i]
            hand_l_pos = convertto(hand_l)
            hand_r_pos = convertto(hand_r)
            l_dis = abs(numbers_pos[0] - hand_l_pos[0]) + abs(numbers_pos[1] - hand_l_pos[1])
            r_dis = abs(numbers_pos[0] - hand_r_pos[0]) + abs(numbers_pos[1] - hand_r_pos[1])
            if l_dis < r_dis :
                answer[i] = 'L'
                hand_l = numbers[i]
            elif l_dis > r_dis :
                answer[i] = 'R'
                hand_r = numbers[i]
            else :
                if hand == "left" :
                    answer[i] = 'L'
                    hand_l = numbers[i]
                if hand == "right" :
                    answer[i] = 'R'
                    hand_r = numbers[i]
    answer = "".join(answer)
    answer = str(answer)
    return answer

numbers = [1, 2]
hand = "left"
print(solution(numbers, hand))
