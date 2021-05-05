def solution(number, k):
    number = list(map(int, number))
    number_s = sorted(number)
    small = number_s[0:k]
    answer = [i for i in number if not i in small or small.remove(i)]
    answer = [str(int) for int in answer]
    answer = "".join(answer)
    return answer

number = "1231234"
k = 3
print(solution(number, k))
