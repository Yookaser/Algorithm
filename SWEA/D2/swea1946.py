# 1946. 간단한 압축 풀기

T = int(input())

for _ in range(T):
    words = '' # 모든 단어들이 저장될 변수
    N = int(input())
    for i in range(N):
        word, number = list(map(str, input().split()))
        words += word * int(number) # 워드를 변환하여 모두 저장

    print(f'#{_ + 1}')

    for i in range(10, len(words), 10):
        print(words[i-10:i])
        if i == len(words): # for else문을 실행하기 위해
            break
    else: # i값이 len(words)와 같지 않은 경우 일부 출력이 생략되는 것을 방지하기 위해
        print(words[i:])