'''

(1, 1) -> (n, m)

1. 아이디어
- BFS
- vertex 개수 최소
X -- 도착 할 수 있는 길: [n-1][m-2] or [n-2][m-1]
X ---> 둘 중 최소값
--> 이동 할 때마다 1씩 더해서, 도착지[n-1][m-1]의 값 구하기
    - 큐 사용 - [0,0] 부터 [n-1, m-1] 까지 최소 거리


2. 시간복잡도
- O(V+E)
- V : 100 * 100
- E : 4V = 4 * 10000
- V+E : 500000 < 2천만 >>> 가능

3. 자료구조
- 그래프 전체 지도 int[][]
- 방문 bool[][]
- Queue(BFS)

'''


from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 미로 리스트 생성
line=''
map = list()
for i in range(n):
    line = input()
    map.append(list(int(line[j]) for j in range(m)))
#print(map)

# 방문 순서 저장 (-1은 방문 안 한 상태)
visited = [[-1] * m for _ in range(n)]

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#BFS
def bfs():
    visited[0][0] = 1 # 현재 칸도 포함

    queue = deque()
    queue.append((0,0))
    #q = [(0,0)] # 현재 위치 넣은 큐 생성
    while queue:
        ey, ex = queue.popleft()
        for k in range(4): # 현재 위치의 상하좌우 살피기
            ny = ey + dy[k]
            nx = ex + dx[k]

            if not (0 <= ny < n and 0 <= nx < m): # 범위 벗어나면 제외
                continue

            if map[ny][nx] == 1 and visited[ny][nx] == -1: # 값 1 && 방문 X
                visited[ny][nx] = visited[ey][ex] + 1
                queue.append((ny, nx))  # 큐에 현재 위치 넣기


bfs()

print(visited[n-1][m-1])




''' 
처음 짰던 코드: list 사용해서 queue 개념을 이용했음.
그러나 pop() 을 쓰면 선입 선출이 안 됨
    마지막 도착지에서, 위에서 아래로 오는 것과 왼쪽에서 오른쪽으로 도착하는 두가지 길이 있으니 
    최소거리 구해보겠다고 따로 아래와 같은 연산을 추가했었음.. (그래도 틀림)
--> 해결::: deque 의 popleft() 사용! 
'''

# if visited[n-2][m-1] == -1: # 둘 중 하나만 길일 경우
#     print(int(visited[n-1][m-2]+1)) # 반대편 길 + 1
# elif visited[n-1][m-2] == -1:
#     print(int(visited[n-2][m-1]+1))
# else: # 둘 다 길일 경우 최소값
#     print(min(visited[n-2][m-1], visited[n-1][m-2])+1)
# print('\n\n\n')
#
# for v in visited:
#     print(v)
#
# # 최소값 if 둘 다 길 else 최대값(양수)
# print(int( min(visited[n-2][m-1], visited[n-1][m-2]) +1) if (visited[n-2][m-1] != -1 and visited[n-1][m-2] != -1) else int(max(visited[n-2][m-1], visited[n-1][m-2])+1))