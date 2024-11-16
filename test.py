def solution(tc, cases):
    fibo = [1, 1]
    for i in range(2, 101):
        fibo.append(fibo[-1] + fibo[-2])
    
    results = []
    
    for N in cases:
        total_sum = sum(fibo[:N]) 
        
        if total_sum % 2 != 0:
            results.append("impossible")
            continue
        
        target_sum = total_sum // 2
        tmp_sum = 0
        result = ["A"] * N 
        
        for i in range(N - 1, -1, -1):
            if tmp_sum + fibo[i] <= target_sum:
                tmp_sum += fibo[i]
                result[i] = "B"
            if tmp_sum == target_sum:
                break
        
        if tmp_sum == target_sum:
            results.append("".join(result))
        else:
            results.append("impossible")
    
    return results


tc = int(input())
cases = [int(input()) for _ in range(tc)]

outputs = solution(tc, cases)

for output in outputs:
    print(output)