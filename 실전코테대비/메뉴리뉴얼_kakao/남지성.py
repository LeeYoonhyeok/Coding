from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for course_len in course:
        combs = []
        
        for order in orders:
            combs.extend(combinations(sorted(order), course_len))
        
        combs_count = Counter(combs)
        
        if combs_count:
            max_count = max(combs_count.values())
            if max_count > 1:
                for comb, count in combs_count.items():
                    if count == max_count:
                        result.append(''.join(comb))
    
    return sorted(result)
                
