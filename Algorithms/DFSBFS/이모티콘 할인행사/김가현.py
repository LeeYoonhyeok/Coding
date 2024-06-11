'''
이모티콘 할인 => 10%, 20%, 30%, 40%
이모티콘 최대 개수: 7개 => level
할인 종류 수 => branch

각 조합에서 user(<=100)들의 정보에 따라
이모티콘 플러스 가입자수와 이모티콘 판매액을 계산.

*시간복잡도
조합 수 4^7 = 2^14 = 16000
조합수 * 유저수 * emoticon 수 = 16000 * 100 * 7 = 약 1200만 

'''
emoticon_plus = 0   # 최대 이모티콘 플러스 가입자 수
sales = 0 # 최대 판매 금액

def check_user(rates, users, emoticons):
    plus_cnt = 0 # 이모티콘 플러스 가입자 수
    sales_money = 0 # 이모티콘 판매액
    length = len(emoticons) # 이모티콘 개수
    
    for user in users: # [할인 비율, 가격]
        amount = 0 # 사용자가 이모티콘에 지출한 금액
        for i in range(length): # 각 이모티콘에 대해
            if user[0] > rates[i]: # 사용자의 할인 기준보다 낮은 할인율은 무시
                continue
            amount += (emoticons[i] * (100-rates[i])) / 100 # 할인이 적용된 금액을 누적
        
        if user[1] <= int(amount): # 사용자가 설정한 지출 한도를 초과하면 이모티콘 플러스 가입
            plus_cnt += 1
        else:
            sales_money += amount # 한도를 초과하지 않으면 판매액 누적
            
    return plus_cnt, int(sales_money)
        

def dfs(level, rates, users, emoticons):
    global emoticon_plus, sales
    if level == len(emoticons):
        plus, money = check_user(rates, users, emoticons)
        if emoticon_plus < plus:
            emoticon_plus = plus
            sales = money
        elif emoticon_plus == plus:
            if sales < money:
                sales = money
        return
    
    for rate in range(10, 41, 10):
        dfs(level + 1, rates + [rate], users, emoticons)
    

def solution(users, emoticons):
    global emoticon_plus, sales
    answer = []
    dfs(0, [], users, emoticons)
    answer = [emoticon_plus, sales]
    return answer
