import sys
input = sys.stdin.readline

def prime_sum(N):
    # 에리토스테네스의 채
    is_prime = [True] * (N+1)
    is_prime[0], is_prime[1] = False, False    
    
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, N+1, i): # 소수의 배수는 소수가 아니므로
                is_prime[j] = False
    primes = [x for x in range(2, N+1) if is_prime[x]]                
    
    tmp_sum = 0
    left, right = 0, 0
    ans = 0
    
    while right < len(primes):        
        if tmp_sum == N:
            ans += 1
            tmp_sum -= primes[left]
            left += 1
        elif tmp_sum > N:
            tmp_sum -= primes[left]
            left += 1
        elif tmp_sum < N:
            tmp_sum += primes[right]
            right += 1
            
    while tmp_sum >= N:
        if tmp_sum == N:
            ans += 1
        tmp_sum -= primes[left]
        left += 1
            
    return ans

N = int(input())
print(prime_sum(N))