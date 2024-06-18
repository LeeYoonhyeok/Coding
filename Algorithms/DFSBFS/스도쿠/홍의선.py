
'''
가로, 세로, 사각형에 각각 들어갈 수 있는 숫자 리스트를 저장
숫자를 어떤 것도 넣을 수 없는 경우면 return (백트래킹)
'''
Map = [list(map(int, input().split())) for _ in range(9)]

Rows = [set([i for i in range(1, 10)]) for _ in range(9)]
Cols = [set([i for i in range(1, 10)]) for _ in range(9)]
Square = [set([i for i in range(1, 10)]) for _ in range(9)]

Zeros = []
for y in range(9):
    for x in range(9):
        if Map[y][x] == 0:
            Zeros.append((y, x))
            continue

        Rows[y].remove(Map[y][x])
        Cols[x].remove(Map[y][x])
        
        # 몇번째 Square인지 구하기
        order = int(y/3)*3
        order += int(x/3)
        Square[order].remove(Map[y][x])

flag = False
def func(level):
    global Map, Rows, Cols, Square, flag

    if level == len(Zeros):
        for y in range(9):
            for x in range(9):
                print(Map[y][x], end=' ')
            print()
        flag = True        
        return
    
    if flag:  # 이미 맵이 완성 되었다면 나가
        return
    
    y, x = Zeros[level]
    for i in range(1, 10):
        if not i in Rows[y]:
            continue
        if not i in Cols[x]:
            continue

        order = int(y/3)*3
        order += int(x/3)
        if not i in Square[order]:
            continue
        
        # 상태 변경
        Rows[y].remove(i)
        Cols[x].remove(i)
        Square[order].remove(i)
        Map[y][x] = i

        func(level + 1)

        # 복구
        Rows[y].add(i)
        Cols[x].add(i)
        Square[order].add(i)

func(0)

        