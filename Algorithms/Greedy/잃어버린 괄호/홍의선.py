'''
플러스들을 미리 다 더해버린다.

'''
equation = input()
num_list = []
op_list = []
num = ''
for i in range(len(equation)):
    if equation[i] == '-' or equation[i] == '+':  # 문자일 경우
        op_list.append(equation[i]) 
        num_list.append(int(num))
        num = ''
    else:  # 숫자일 경우
        num += equation[i]
        
num_list.append(int(num))

index = 0
while index < len(op_list):
    if op_list[index] == '+':
        num_list[index] = num_list[index] + num_list[index+1]
        num_list.pop(index+1)
        op_list.pop(index)
    else:
        index += 1

index = 0
while index < len(op_list):
    if op_list[index] == '-':
        num_list[index] = num_list[index] - num_list[index+1]
        num_list.pop(index+1)
        op_list.pop(index)
    else:
        index += 1

print(num_list[0])