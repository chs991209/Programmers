#1. 아직 완전히 이해는 못함

def solution(numbers, target) :
    tree = [0]
    for i in numbers :
        sub_tree = []
        for j in tree :
            sub_tree.append(j + i)
            sub_tree.append(j - i)
        tree = sub_tree
    return tree.count(target)

# 출처: https://train-validation-test.tistory.com/entry/Programmers-level-2-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-python

#2. numbers 리스트를 변화시키는 방법
def dfs(numbers, target, depth) :
    count = 0
    if depth < len(numbers) :
        count = count + dfs(numbers, target, depth + 1)
        numbers[depth] = -1 * numbers[depth]
        count = count + dfs(numbers, target, depth + 1)
        return count
    elif depth == len(numbers) :
        if sum(numbers) == target :
            return 1
        return 0

def solution(numbers, target) :
    answer = dfs(numbers, target, 0)
    return answer

# 출처: ..
