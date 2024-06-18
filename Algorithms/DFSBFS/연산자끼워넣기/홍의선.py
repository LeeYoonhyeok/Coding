N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))

ans_max = -0x7fffffff
ans_min = 0x7fffffff
def func(level, val):
    global N, A, OP, ans_max, ans_min

    if level == N-1:
        if val >= ans_max:
            ans_max = val
        if val <= ans_min:
            ans_min = val
        return

    # +
    if OP[0] > 0:
        OP[0] -= 1
        res = val + A[level+1]
        func(level + 1, res)
        OP[0] += 1
    # -
    if OP[1] > 0:
        OP[1] -= 1
        res = val - A[level+1]
        func(level + 1, res)
        OP[1] += 1
    # x
    if OP[2] > 0:
        OP[2] -= 1
        res = val * A[level+1]
        func(level + 1, res)
        OP[2] += 1
    # /
    if OP[3] > 0:
        OP[3] -= 1
        if val < 0:
            val *= -1
            res = int(val / A[level+1])
            res *= -1
        else:
            res = int(val / A[level+1])
        func(level + 1, res)
        OP[3] += 1

func(0, A[0])
print(ans_max)
print(ans_min)