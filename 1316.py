'''
1. 아이디어
- 2중 for => 이전 글자 != 현재 글자
            and 현재 글자 in 알파벳 => False
- True 개수

2. 시간복잡도
- 2중 for 문

3. 자료구조
- list 단어
- bool[]
- list 알파벳 temp 용도
'''

import sys
input = sys.stdin.readline

n = int(input())
words = list(input().rstrip() for _ in range(n))
# print(words)

alphabet = list() # 나왔었던 알파벳 저장
chk = [True] * n
# print(chk)

for i in range(n):
    alphabet.append(words[i][0])
    for j in range(1, len(words[i])):
        if words[i][j-1] != words[i][j]:    # 이전과 다른 글자인데
            if words[i][j] in alphabet:     # 이미 나왔던 글자
                chk[i] = False
            else:                            # 안 나왔던 글자
                alphabet.append(words[i][j]) # 알파벳 풀에 추가
    # print(alphabet)
    alphabet.clear() # 이번 단어 끝났으니 전체 삭제

# print(alphabet)
# print(chk)
print(chk.count(True)) # True 개수 반환
