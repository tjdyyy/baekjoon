'''
1. 아이디어
- while 문, 특정 조건 종료될 때까지 반복
- 4방향 for문 탐색
- 더이상 탐색 불가능 -> 뒤로 한 칸 후진
- 후진 불가 -> 종료

2. 시간복잡도
- O(n*m) : 50^2 < 2억

3. 자료구조
- map : int[][]
- 로봇 청소기 위치, 방향, 전체 청소한 곳 수
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x] == 0:
        map[y][x] = 2 # 청소 완
        cnt += 1
    sw = False
    for i in range(1, 5): # 4방향
        # print("d-i", d-i)
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0: # 청소하지 않은 곳
                # 회전
                d = (d-i+4)%4 # d 양수로 유지
                # 한 칸 전진
                y = ny
                x = nx
                sw = True
                # 1번으로 ==> while 문 처음으로
                break

    # 4방향 모두 있지 않은 경우
    if not sw: # for문 break 하고 여기로 오지 않게 sw 값 설정
        # 바라보는 방향 유지, 후진 1칸 - 뒤쪽 막혀있으면 스탑
        # 뒤쪽 방향 막혀있는지 확인
        ny = y - dy[d] # 뒤로 가기: 현재 바라보고 있는 방향을 뺌
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1: # 막힌 경우
                break
            else: # 뒤로 후진
                y = ny
                x = nx
            # 2번으로 돌아가기 ==> 1번으로 가는 거 아님
            # (이미 청소 했으니 이제 청소 안 해야 됨)
            # ==> while 문 바로 밑 1번을 청소 안 된 경우에만 청소 해주기로 바꾸기
        else:
            break


print(cnt)
