'''
각 이모티콘의 할인 % 종류는 4가지이다. 
10%, 20%, 30%, 40%

이모티콘의 최대 개수는 7개 이므로
level은 이모티콘 개수
branch는 할인 종류수

각 조합에서 user(<=100)들의 정보에 따라 
이모티콘 플러스 가입자수와 이모티콘 판매액을 계산한다.

*시간복잡도
조합수 = 4^7 = 2^14 = 16000
조합수 * 유저수 * emoticon 수= 16000 * 100 * 7 = 약 1200만

'''
emoticon_plus = 0
sales = 0

def check_users(rates, users, emoticons):
    #  시간복잡도 : users * rates = 100 * 7 = 700
    plus_cnt = 0  # 이모티콘 플러스 가입자 수
    sales_money = 0
    length = len(emoticons)  # 이모티콘 개수
    
    for user in users:  # [할인 비율, 가격]
        amount = 0
        for i in range(length):
            if user[0] > rates[i]:
                continue
            amount += (emoticons[i]*(100-rates[i]))/100
        
        if user[1] <= int(amount):
            plus_cnt += 1
        else:
            sales_money += amount
    
    return plus_cnt, int(sales_money)
        
            

    
def dfs(level, rates, users, emoticons):
    global emoticon_plus, sales
    if level == len(emoticons):
        # user들 비교
        plus, money = check_users(rates, users, emoticons)
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

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))