def solution(expression):
    num = 0
    s_exp = []
    for e in expression :
        if '0' <= e <= '9' :
            num = num * 10 + int(e)
        elif e in ['*', '+', '-'] :
            s_exp.append(num)
            s_exp.append(e)
            num = 0
    s_exp.append(num)

    case = [[0], [1], [2], [3], [4], [5], [6]]
    case[1] = [0, '*', '+', '-']
    case[2] = [0, '*', '-', '+']
    case[3] = [0, '+', '*', '-']
    case[4] = [0, '+', '-', '*']
    case[5] = [0, '-', '*', '+']
    case[6] = [0, '-', '+', '*']
    answer = [-1, 1, 2, 3, 4, 5, 6]
    
    for no in [1, 2, 3, 4, 5, 6]: 
        c_exp = s_exp.copy()
        for operator in [1, 2, 3] :
            i = 0
            while i < len(c_exp):
                if c_exp[i] == case[no][operator]:
                    c_exp[i-1] = eval(str(c_exp[i-1])+case[no][operator]+str(c_exp[i+1]))
                    c_exp.pop(i)
                    c_exp.pop(i)
                else :
                    i += 1
            answer[no] = abs(c_exp[0])
    return max(answer)

print(solution("50*6-3*2"))
