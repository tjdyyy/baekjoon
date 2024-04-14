'''

1. 아이디어
- 2중 for => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : m * n = 500 * 500
- E : 4V = 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < (파이썬 연산 1초에) 2억 => (문풀) 가능! (파이썬 1초에 2천만이라는데? 암튼 가능)

3. 자료구조
- 그래프 전체 지도 : int[][] (1과 0으로 이루어졌으니)
- 방문 : bool[][]
- Queue(BFS)

'''

# 습관처럼 써주기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] # 변수 없이 반복문 사용
# print(map)
chk = [[False] * m for _ in range(n)] # 방문 여부 확인 - 초기값 False

# 이건 외워두는 게 빠름
dy = [0,1,0,-1]
dx = [1,0,-1,0]
    # 우 하 좌 상

def bfs(y, x): # 그림 사이즈 구해야 함
    rs = 1 # 이번 그림 크기
    q = [(y, x)] # 현재 위치 넣은 큐 생성
    while q:
        ey, ex = q.pop()
        for k in range(4): # 현재 위치의 상하좌우 살피기
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # 인덱스가 범위 내인지 확인
                if map[ny][nx] == 1 and chk[ny][nx] == False: # 1인데 방문 안 한 곳
                    rs += 1 # 사이즈 +1
                    chk[ny][nx] = True # 방문했음
                    q.append((ny,nx)) # 큐에 현재 위치 넣기
    return rs

cnt = 0
maxv = 0
for j in range(n): # 세로
    for i in range(m): # 가로
        if map[j][i] == 1 and chk[j][i] == False: # 1인데 방문 안 한 곳
            chk[j][i] = True # 방문했다
            # 전체 그림 개수 +1
            cnt += 1
            # BFS -> 그림 크기 구해주기
            # 최대값 갱신
            maxv = max(maxv, bfs(j,i)) # 현재 최대값과 현재 위치 BFS해서 얻은 그림 크기 중 큰 값으로 갱신

print(cnt)
print(maxv)