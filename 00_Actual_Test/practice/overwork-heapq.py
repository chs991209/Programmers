import heapq

heap = []

def solution(n, works) :
    for i in range(len(works)) :
        heapq.heappush(heap, -works[i])
    cnt = 0
    while heap and cnt < n :
        a = -heapq.heappop(heap)
        if a > 0 :
            a -= 1
            cnt += 1
            heapq.heappush(heap, -a)
        #if cnt == n :
            #break
    answer = 0
    
    i = 0
    k = len(heap)
    while k - i > 0 :
        answer += heap[i] * heap[i]
        i += 1
    return answer
