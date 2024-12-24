import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

end_times = []

for start, end in lectures:
    if end_times and end_times[0] <= start:
        heapq.heappop(end_times)
        
    heapq.heappush(end_times, end)
    
print(len(end_times))