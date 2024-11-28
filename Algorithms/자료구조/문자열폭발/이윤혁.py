import sys
input = sys.stdin.readline

def find_st(st, boom):    
    boom_len = len(boom)
    stack = []
    
    for char in st:
        stack.append(char)
        if len(stack) >= boom_len and ''.join(stack[-boom_len:]) == boom:
            for _ in range(boom_len):
                stack.pop()
    
    return ''.join(stack) if stack else "FRULA"
st = input().rstrip()
boom_word = input().rstrip()
print(find_st(st, boom_word))