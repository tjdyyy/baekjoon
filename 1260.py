'''
1. 아이디어
- DFS: 재귀함수
- BFS: 2중 for

2. 시간복잡도
- O(V+E) = O(5N*M) = O(5*1000*10000) < 2억

3. 자료구조
- 그래프 전체 지도 int[][]
- 방문 여부 bool[] -> 각 1개
- bfs >> deque 사용
'''

import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)] # 0번째 인덱스 사용 X (인덱스 = 정점)
# * 로 생성 시 shallow copy --> list comprehension 사용
# graph = [[0]*(n+1)]*(n+1)
# print(graph)

# 연결된 정점은 1 입력
for _ in range(m):
    y, x = map(int, input().split())
    graph[y][x] = 1
    graph[x][y] = 1
print(graph)

chkd = [False] * (n+1)
chkb = [False] * (n+1)


def dfs(v):
    chkd[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not chkd[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    chkb[v] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not chkb[i] and graph[v][i] == 1:
                q.append(i)
                chkb[i] = True

dfs(v)
print()
bfs(v)
