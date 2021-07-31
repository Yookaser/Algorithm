# 5525. IOIOI

N = int(input())
M = int(input())

ioi = input()
result = 0 # 결과를 저장할 변수(N 개수)
cnt = 0 # 중간 결과를 저장할 변수('IOI' 개수 카운팅)
i = 1

while i < M-1:
    if ioi[i-1:i+2] == 'IOI': # 3칸씩 'IOI'인지 검사
        cnt += 1 # 'IOI'이므로 카운팅
        i += 1 # 만약 'IOI'이면, i가 +1만 되면, 'O'부터 시작되므로 안됨(그러므로 여기서 +1하고, 이것 때문에 while로 구현)
        if cnt == N: # cnt가 N만큼 누적되면, 'I' + 'OI'*N이 됨!
            result += 1 # 결과 +1
            cnt -= 1 # 중간 결과 -1('IOIOI'에는 'IOI'가 2개 있다는 걸 구현해야 함)
    else: # 'IOI'가 아닌 경우
        cnt = 0 # 아니므로 0으로 만들어야 함
    i += 1 # i 증가시킴 ==> 만약, 'IOI'라서 if에 걸렸으면 총 2가 증가하게 되는 것

print(result)