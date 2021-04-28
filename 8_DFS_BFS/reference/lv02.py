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
