def solution(targets):
    answer = 0
    prev = -1
    targets.sort(key=lambda x: x[1])
    
    for start, end in targets:
        if start >= prev:
            prev = end
            answer += 1
    
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))
