
'''
#case1
두 사람이 선물을 주고받은 기록이 있다면, 
이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.

#case2
두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 
선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.

딕셔너리 만든 후 완전탐색
'''
def solution(friends, gifts):
    answer = 0
    
    # dictionary 만들기
    connect = dict()
    for friend in friends:
        connect[friend] = []
    for gift in gifts:
        giving, taking = gift.split()
        connect[giving].append(taking)
        
    # 선물지수 구하기
    gift_index = dict()
    for friend in friends:
        give_cnt, take_cnt = 0, 0
        for key, value in connect.items():
            if key == friend:
                give_cnt = len(value)
            else:
                take_cnt += value.count(friend)
        
        gift_index[friend] = give_cnt - take_cnt    

    # find answer
    for friend in friends:
        temp_answer = 0
        for giving in friends:
            
            if friend == giving:
                continue 
            # 주고 받은 개수 구하기
            giving_cnt = connect[friend].count(giving)
            taking_cnt = 0
            if giving in connect:
                if friend in connect[giving]:
                    taking_cnt = connect[giving].count(friend)

            # 다음달에 받아야 할 선물 개수 카운트 시작
            if giving_cnt > 0 and taking_cnt == 0: # 주기만한 경우 (case2)
                temp_answer += 1
                continue        
            
            if giving_cnt == taking_cnt: # 주고 받은 수가 같다면 || 주고받지 않은 경우 (case2)
                if gift_index[friend] > gift_index[giving]: # 선물지수 비교
                    temp_answer += 1
                    continue
                    
            if giving_cnt > taking_cnt: # 주고 받은 수가 다르다면 (case1)
                temp_answer += 1
                continue                             
        
        answer = max(answer, temp_answer)
    return answer


friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends, gifts))
# 4