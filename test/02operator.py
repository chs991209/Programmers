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

    case1 = 0 # * > + > -
    case2 = 0 # * > - > +
    case3 = 0 # + > * > -
    case4 = 0 # + > - > *
    case5 = 0 # - > * > +
    case6 = 0 # - > + > *
    j = 0
    for i in range(0, len(s_exp)) :
        if s_exp[i] == '*' :
            case1[j] = s_exp[i-1] * s_exp[i+1]
            j += 1
            i += 2
    for i in range(0, len(s_exp)) :
        if s_exp[i] == '+' :
            case1[j] = s_exp[i-1] + s_exp[i+1]
            j += 1
            i += 2
    return max(case1, case2, case3, case4, case5, case6)

print(solution("100+30*9"))
