# 2559. 수열

N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

start, end = 0, K # 시작, 끝(투포인터)
result = temp = sum(arr[:end]) # 초기값 지정(0~(end-1)의 합)

while end < N: # end가 N-1까지
    temp -= arr[start] # 시작값 빼기
    temp += arr[end] # 끝값 더하기
    end += 1
    start += 1
    if temp > result: # temp
        result = temp

print(result)