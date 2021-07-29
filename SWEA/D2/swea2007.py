# 2007. 패턴 마디의 길이

def pattern(arr):
    result = 0

    for i in range(1, 10): # 패턴이 없다는 조건은 없고, 패턴의 최대 길이는 10이므로 범위는 1~10(패턴은 작은 것부터 찾아야 함!)
        for j in range(i, 30, i): # 시작은 i, 끝은 30, 순차는 i(이 문제에서는 끝을 30 - (30 % i)로 설정하면 if문 필요 없음 -> 하지만 히든 케이스(SAMSUNGSAMSUNGSAMSUNGSAMSUNGSE)를 생각하면 필요함)
            if j + i > 30 and arr[j:] == arr[:-j]: # i가 모두 30의 약수가 아니므로, 마지막 값은 다르게 나올 수 있는데, 이 경우를 처리(단, 남은 부분이 반복중인 경우만, 아니면 elif에 걸림)
                continue
            elif arr[j - i:j] != arr[j:j + i]: # 반복 여부를 확인(아니면 바로 break하여 시간 절약)
                break
        else: # 만약 for문을 무사히 나온다면, 패턴이 있다는 것이므로 result 값을 i로 지정
            result = i
            break

    return result

T = int(input())

for _ in range(T):
    str_list = input()

    print(f'#{_ + 1} {pattern(str_list)}')