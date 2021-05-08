def solution(n, k, cmd):
    answer = ['O'] * n
    name = []
    for nam in range(0, n) :
        name.append(nam)
    #name = ['무지', '콘', '어피치', '제이지', '프로도', '네오', '튜브', '라이언']
    select_ = name[k]
    delete_ = []
    delete_i = []
    for i in range(0, len(cmd)) :
        if cmd[i][0] == 'U' :
            num = int(cmd[i][2])
            j = name.index(select_)
            select_ = name[j-num]
            print("u name= ", select_)
            print("u index= ", j-num)

        elif cmd[i][0] == 'D' :
            num = int(cmd[i][2])
            j = name.index(select_)
            select_ = name[j+num]
            print("d name= ", select_)
            print("d index= ", j+num)

        elif cmd[i][0] == 'C' :
            j = name.index(select_)
            if j == len(name)-1 :
                select_ = name[j]
                delete_.append(select_)
                delete_i.append(j)
                answer[j] = 'X'
                name.remove(select_)
                select_ = name[-1]
                print("c max name= ", select_)
                print("c max index= ", name.index(select_))
            else :
                select_ = name[j]
                delete_.append(select_)
                delete_i.append(j)
                answer[j] = 'X'
                name.remove(select_)
                select_ = name[j]
                print("c name= ", select_)
                print("c index= ", name.index(select_))

        elif cmd[i][0] == 'Z' :
            j = name.index(select_)
            zname = delete_.pop(-1) # name
            zidx = delete_i.pop(-1) # index
            name1 = name[0:zidx]
            name2 = name[zidx:]
            name = name1 + [zname] + name2
            answer[zidx] = 'O'
    answer = "".join(answer)
    answer = str(answer)
    return answer

print(solution(8, 2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
