def hash(x):
    aaa = 0
    for c in x:
        aaa += ord(c)  
    return aaa % 10000

def solution(participant, completion):
    hash_table = [[] for _ in range(10000)]

    for c in completion:
        c_hash = hash(c)
        hash_table[c_hash].append(c)

    for p in participant:
        p_hash = hash(p)
        if not p in hash_table[p_hash] :
            return p
        else :
            hash_table[p_hash].remove(p)
