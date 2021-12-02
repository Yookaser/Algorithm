# 11721. 열 개씩 끊어 출력하기

word = input()
for i in range(0, len(word), 10):  # 10개씩 끊기
    print(word[i:i+10])
