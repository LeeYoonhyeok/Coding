'''
course 개수로 order의 조합을 만들어 정렬 후 딕셔너리 카운트
'''
from itertools import combinations

def solution(orders, course):
    answer = []  
    for count in course:
        order_dict = dict()
        for order in orders:
            combi = combinations(order, count)
            for com in combi:
                com = tuple(sorted(com))
                if com in order_dict:
                    order_dict[com] += 1
                else:
                    order_dict[com] = 1
        tmp_ans = [k for k,v in order_dict.items() if max(order_dict.values()) == v and 
                   max(order_dict.values()) != 1]
        for tmp in tmp_ans:
            answer.append(''.join(tmp))
    return answer
    
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]
print(solution(orders, course))
# result = ["AC", "ACDE", "BCFG", "CDE"]