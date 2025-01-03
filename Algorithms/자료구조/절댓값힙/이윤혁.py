import heapq
import sys
input = sys.stdin.readline

n = int(input())
pos_numbers = []
neg_numbers = []
for _ in range(n):
    x = int(input())
    if x == 0: # pop
        if pos_numbers or neg_numbers:
            if not pos_numbers:
                print(-heapq.heappop(neg_numbers))
            elif not neg_numbers:
                print(heapq.heappop(pos_numbers))
            else: # 둘 다 있을 경우
                if pos_numbers[0] == neg_numbers[0]:
                    print(-heapq.heappop(neg_numbers))
                elif pos_numbers[0] > neg_numbers[0]:
                    print(-heapq.heappop(neg_numbers))
                elif pos_numbers[0] < neg_numbers[0]:
                    print(heapq.heappop(pos_numbers))
        else:
            print("0")
            
    else: # push
        if x > 0:
            heapq.heappush(pos_numbers, x)
        elif x < 0:
            heapq.heappush(neg_numbers, -x)