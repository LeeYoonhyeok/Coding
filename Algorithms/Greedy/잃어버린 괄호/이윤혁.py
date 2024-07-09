import sys
equation = sys.stdin.readline()
ans = 0
check_minus = False
tmp_num = ''
for i in range(len(equation)):
    if equation[i] == '-':
        if check_minus:
            ans -= int(tmp_num)
        elif not check_minus:
            ans += int(tmp_num)
            check_minus = True
        tmp_num = ''
        
    elif equation[i] ==  '+':
        if check_minus:
            ans -= int(tmp_num)
        elif not check_minus:
            ans += int(tmp_num)
        tmp_num = ''
    else:
        tmp_num += equation[i]

if tmp_num:
    if check_minus:
        ans -= int(tmp_num)
    else:
        ans += int(tmp_num)
print(ans)