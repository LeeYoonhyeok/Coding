
# 입력 받는 것들
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

# 초기값
max_val = -1e9
min_val = 1e9

def dfs(level, cur_val):
    global max_val, min_val

    # 끝까지 가면 max, min값 갱신
    if level == N:
        max_val = max(max_val, cur_val)
        min_val = min(min_val, cur_val)
        return
    
    # 탐색
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            next_val = cur_val

            # 더하기, 빼, 곱, 나
            if i == 0:
                next_val += nums[level]
            elif i == 1:
                next_val -= nums[level]
            elif i == 2:
                next_val *= nums[level]
            elif i == 3:
                if next_val < 0:
                    next_val = -(-next_val // nums[level])
                else:
                    next_val //= nums[level]
            
            dfs(level + 1, next_val)

            ops[i] += 1   # 연산자 다시 쓸 수 있게 복원

dfs(1, nums[0])



print(max_val)
print(min_val)