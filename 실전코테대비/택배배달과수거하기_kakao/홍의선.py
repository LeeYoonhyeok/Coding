'''
가장 멀리있는 집부터 왼쪽으로 택배개수 합산(cap 이하일 때 까지)
가장 멀리있는 집부터 왼쪽으로 수거택배 개수 합산(cap 이하일 때 까지)

두 가지 경우에서 더 멀리있는 집의 위치 * 2 가 이동거리가 될 것이다.
이렇게 모든 집을 탐색할 때까지 반복

'''
def optimize(d_pos, r_pos, deliveries, pickups):  # 가장 왼쪽의 집이 배달 및 수거가 0이 아니도록 최적화
    while deliveries[d_pos] == 0 and d_pos >= 0:
        d_pos -= 1

    while pickups[r_pos] == 0 and r_pos >= 0:
        r_pos -= 1
    
    return d_pos, r_pos

def update_position(d_pos, r_pos, cap, deliveries, pickups):
    current_boxes = 0
    while d_pos >= 0:
        # 해당 집 배달 개수를 더했을 때, 최대 보관할 수 있는 택배 개수를 넘기는지?
        sum_boxes = deliveries[d_pos] + current_boxes
        
        if sum_boxes > cap:
            # 현재위치는 한번에 모든 택배를 배달하진 못하지만, cap에 저장할 수 있는데까지 일부 배달 가능
            deliveries[d_pos] -= (cap - current_boxes)
            break 
        
        d_pos -= 1
        current_boxes = sum_boxes
    
    current_boxes = 0    
    while r_pos >= 0:
        # 해당 집 배달 개수를 더했을 때, 최대 보관할 수 있는 택배 개수를 넘기는지?
        sum_boxes = pickups[r_pos] + current_boxes
        
        if sum_boxes > cap:
            pickups[r_pos] -= (cap - current_boxes)
            break 
        
        r_pos -= 1
        current_boxes = sum_boxes        
    
    return d_pos, r_pos 
    
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_pos = n - 1  # 가장 멀리있는 배달할 집 위치
    r_pos = n - 1  # 가장 멀리있는 수거할 집 위치
    
    d_pos, r_pos = optimize(d_pos, r_pos, deliveries, pickups)  
    
    while d_pos >= 0 or r_pos >= 0:
        answer += (max(d_pos+1, r_pos+1) * 2)
        d_pos, r_pos = update_position(d_pos, r_pos, cap, deliveries, pickups)
        
        
    return answer

cap = 1
n = 1
deliveries = [0]
pickups = [0]
print(solution(cap, n, deliveries, pickups))

