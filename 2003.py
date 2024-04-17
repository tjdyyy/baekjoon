'''
1. 아이디어
- while 문, 포인터는 N 범위 내
    - 합 < M : 오른쪽 ++
    - 합 = M : cnt++, 오른쪽 ++
    - 합 > M : 왼쪽 ++

2. 시간복잡도
- O(n)

3. 자료구조
- 수열 int[]
- 왼쪽/오른쪽 포인터(인덱스) int
- cnt
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
hap = 0
cnt = 0
lPointer = 0
rPointer = 1 # slicing 할 때 마지막 인덱스 -1이므로

# 왼쪽 <= 오른쪽
# hap < M : 오른쪽++
# hap = M : cnt++, 오른쪽++
# hap > M : 왼쪽++
while rPointer <= N and lPointer <= rPointer:
    hap = sum(nums[lPointer:rPointer])
    if hap == M:
        cnt += 1
        rPointer += 1
    elif hap < M:
        rPointer += 1
    else:
        lPointer += 1
print(cnt)

'''
# 2. 시간 초과 - 2중 for문, sum, slicing

for i in range(N):

    for j in range(i, N):
        hap = sum(nums[i:j+1])
        # print("hap", hap, "(",i, j, ")")
        if hap == M:
            cnt += 1
            # print("cnt  i   j")
            # print(cnt, i, j, sep="\t")
            break
        elif hap > M: break

print(cnt)
'''

'''
# 1. 시간 초과 - 2중 for문

for i in range(N):
    hap = nums[i]
    if hap == M:
        cnt += 1
        # print("혼자", i, cnt)
        continue
    # print(i,'  ', hap)
    for j in range(i+1, N):
        hap += nums[j]
        # print(i, j, hap)
        if hap == M:
            cnt += 1
            # print("cnt", cnt)
            break
        elif hap > M: break

print(cnt)
'''