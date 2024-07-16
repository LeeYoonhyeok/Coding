'''
더 큰 큐에서 무조건 더 작은 큐로 이동한다면?

*불가능 조건
-> 불가능한 경우는 2, 2 와 3 이면
2 / 3 2
2 3 / 2
3 / 2 2
3 2 / 2
2 / 2 3 
2 2 / 3..
2 / 3 2
원상 복구 되면 불가능..? 근데 원소가 많을 경우 원상 복구될 때 까지 기다리려먼 많은 시간 걸릴 듯
원소 길이를 초과하면 불가능..? 큐 길이가 30만이니까 최대 60만까지만 보면 된다..
해보자
-> 시간 초과...

불가능 조건을 더 빠르게 판별할 방법..

'''
def get_sum_q(q):
    val = 0
    for v in q:
        val += v
    return val 

def solution(queue1, queue2):
    answer = -1
    q1_val = get_sum_q(queue1)
    q2_val = get_sum_q(queue2)
    q1_index = 0
    q2_index = 0
    length = len(queue1) + len(queue2)
    cnt = 0
    while cnt <= (length+10):  # +10 은 무슨 기준인지 모르겠음..

        if q1_val == q2_val:
            answer = cnt 
            break
        elif q1_val > q2_val:  # queue1 이 더 큰 경우
            head = queue1[q1_index]
            q1_index += 1
            queue2.append(head)
            
            q1_val -= head
            q2_val += head 
        else:  # queue2 가 더 큰 경우
            head = queue2[q2_index]
            q2_index += 1 
            queue1.append(head)
            
            q2_val -= head
            q1_val += head
        
        cnt += 1
            
    return answer

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))