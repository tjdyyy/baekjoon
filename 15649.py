'''
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문 여부 확인)
- 재귀함수에서 m개를 선택할 경우 print

- for 1~N 중 하나 선택 + 방문 여부 체크
- 결과값에 추가 + 방문 여부 체크
- 재귀함수 호출

2. 시간복잡도
- N! >> 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)    # 다음 호출하고
            chk[i] = False  # 돌아오면 chk 다시 복구
            rs.pop()        # rs 도 복구

recur(0)
