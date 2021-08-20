# 5356. 의석이의 세로로 말해요

# 방법1. 

T = int(input())
for test in range(T):
    arr = []
    result = ''

    for i in range(5):  # 입력을 2차원 리스트로 저장
        word = list(input())
        for i in range(15-len(word)):  # 빈 칸은 공백으로 채움
            word.append('')
        arr.append(word)

    for i in zip(*arr):  # 결과 형태로 변환
        result += ''.join(i)

    print('#{} {}'.format(test+1, result))

# 방법2.

# T = int(input())
# for test in range(T):
#     result = ''

#     word = [list(input()) for _ in range(5)]

#     for j in range(15):  # 최대 길이만큼 반복(열)
#         for i in range(15):  # 최대 길이만큼 반복(행)
#             try:
#                 result += word[i][j]
#             except IndexError:
#                 pass

#     print('#{} {}'.format(test+1, result))
