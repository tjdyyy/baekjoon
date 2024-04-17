'''
1. 아이디어
- 투포인터 활용
- for 문, 처음에 k개 값 저장
- 다음 인덱스 더해주고, 이전 인덱스 빼줌
- 이때마다 최대값 갱신

2. 시간복잡도
- O(N) = 1e5 => 가능

3. 자료구조
- 각 숫자들 n개 저장 배열 : int[]
    - 숫자들 최대 100 => int 가능
- k개 값 저장할 변수 : int
    - 최대 : k * 100 = 1e5 * 100 = 1e7 => int 가능
- 최대값 : int
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0

# k개 더해주기
for i in range(K):
    each += nums[i]
maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
    # 시작: 0~k-1 번까지 더해져 있음(each) -> k~n까지 인덱스 돌아야함
for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)