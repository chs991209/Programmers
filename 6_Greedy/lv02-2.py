def solution(number, k):
    same_num = number.replace(number[0], '')
    if not same_num :
        return number[0] * (len(number) - k)
    restart = True
    while restart :
        restart = False
        for i in range(0, len(number) - 1) :
            if k > 0 and number[i] < number[i + 1] :
                number = number.replace(number[i], '', 1)
                k -= 1
                restart = True
                break
    while k > 0 :
        if number[-1] > number[-2] :
            number = number.replace(number[-2], '', 1)
            k -= 1
        else :
            number = number.replace(number[-1], '', 1)
            k -= 1

    return number

number = "12323"
k = 2

print(solution(number, k))

"""
자기 바로 뒤가 자기보다 크면 삭제.
삭제 했으면 그 앞부터 다시 시작.(처음부터 시작 아님)

41235 OK
43215 OK

"77779", 1, "7779"
"77776", 1, "7777"
"77777", 1, "7777"

"1000", 2, "10"

6664177252841이면,
1<7 이므로 1 삭제
4<7 이므로 4 삭제
6<7 이므로 6 삭제
"""

