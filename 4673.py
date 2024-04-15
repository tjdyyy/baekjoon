'''
1. 아이디어
- 전체: 1 ~ 10000
- d(n)으로 생성된 수: generated
- 셀프 넘버: 전체 - generated

2. 시간복잡도
- O(N^2)

3. 자료구조
- set
'''

all_num = set(range(1,10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):        # 문자열처럼 똑똑 떼어서 원래 수 i에 더해주기
        i += int(j)
    generated_num.add(i)

self_num = sorted(all_num - generated_num)
for i in self_num:
    print(i)

