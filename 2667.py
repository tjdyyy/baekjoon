'''
1. 아이디어
- 2중 for, 1 and 방문 x => DFS
- 재귀 함수 (DFS) 찾은 값 정렬 후 출력

2. 시간 복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 2억보다 작으니 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]
'''

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
each = 0
dy = [0, 1, 0, -1] # 4방향 (3시 6시 9시 12시)
dx = [1, 0, -1, 0]

#print(map)

def dfs(y, x):
    global each # 전역변수
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True # 방문 체크
                dfs(ny, nx)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            # DFS 로 크기 구하기 - 크기 받아오는 거 보다 전역변수 사용하는 게 편함
            # ( BFS: 함수 호출, 리턴값으로 크기 반환 )
            each = 0
            dfs(j, i)
            # 크기를 결과 리스트에 넣기
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)