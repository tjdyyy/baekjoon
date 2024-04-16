'''
* 아이디어
- 문서 중요도 queue
- <반복문>
- 현재 문서의 중요도가 최대면 출력, cnt+=1
    - 궁금했던 문서였으면(M==0) loop 탈출
    - 아니면 궁금한 문서 인덱스(M) -1
- 최대 아니면 뒤로 보내기
    - 궁금했던 문서였으면 -> 맨뒤 (M = len -1)
    - 아니었으면 M -1
'''

import sys
input = sys.stdin.readline

from collections import deque

# 테스트 케이스 수 만큼
for _ in range(int(input().rstrip())):
    N, M = map(int, input().split()) # 문서 개수, 궁금한 문서의 인덱스
    print("n=", N, "m=", M)
    priority = deque(map(int, input().split()))
    print(priority)
    cnt = 0

    while priority:
        np = priority[0] # 가장 앞 문서의 중요도

        # np 가 최대면 출력, cnt+=1
        if np >= max(priority):
            cnt += 1
            priority.popleft()
            print(np, "출력")
            # 궁금했던 문서였다면
            if M == 0:
                # print(1, M, priority, cnt)
                break
            M -= 1
            # print(2, M, priority, cnt)


        # 최대 아니면, 뒤로 보내기
        else:
            priority.popleft()
            priority.append(np)
            if M == 0:
                M = len(priority) - 1
                # print(M, priority, cnt)
            else:
                M -= 1
            # print(3, M, priority, cnt)

        # print(M, priority, cnt)

    print(cnt)
