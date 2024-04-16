'''
1. 아이디어
- 재귀함수: for 1~n 선택
- + 다음 수 선택: 이미 선택한 값이 아닌 경우
- m 개 선택할 경우 출력

2. 시간복잡도
- O(N!)

3. 자료구조
- 방문 여부 bool[]
- 선택한 값 입력할 배열 int[]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if len(rs) == M:
        print(' '.join(map(str, rs)))
        return

    for i in range(num+1, N+1):
        if not chk[i]:      # 방문 안 한 곳
            chk[i] = True   # 방문 표시
            rs.append(i)
            recur(i)    # 다음 수 호출 (num+1 ~ N)
            # 함수 호출 후 되돌아오면
            chk[i] = False
            rs.pop()

recur(0)