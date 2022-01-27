def solution(s):
    answer = []
    i = 0
    while i < len(s):
        if "0" <= s[i] <= "9":
            answer.append(s[i])
            i += 1
        elif s[i] == "z":
            answer.append("0")
            i += 4            
        elif s[i] == "o":
            answer.append("1")
            i += 3            
        elif s[i] == "t":
            if s[i + 1] == "w":
                answer.append("2")
                i += 3
            elif s[i + 1] == "h":
                answer.append("3")
                i += 5                
        elif s[i] == "f":
            if s[i + 1] == "o":
                answer.append("4")
                i += 4
            if s[i + 1] == "i":
                answer.append("5")
                i += 4                
        elif s[i] == "s":
            if s[i + 1] == "i":
                answer.append("6")
                i += 3
            elif s[i + 1] == "e":
                answer.append("7")
                i += 5                
        elif s[i] == "e" and s[i + 1] == "i":
            answer.append("8")
            i += 5            
        elif s[i] == "n":
            answer.append("9")
            i += 4
    joinedtoint_answer = int("".join(answer))  
    return joinedtoint_answer
print(solution("threezero123one"))
