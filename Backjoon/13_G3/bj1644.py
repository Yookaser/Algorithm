# 1644. 소수의 연속합

N = int(input())
pc = [True] * (N+1)

for i in range(2, int(N**0.5)+1):  # 에라토스테네스의 체
    if pc[i]:
        pc[2*i::i] = [False] * (N//i-1)  # 시간 단축의 핵심

pl = [0] + [i for i, v in enumerate(pc) if v and i>1]  # 앞의 0 추가(처음부터 e까지의 합을 구하는 것도 있어야 함)
for i in range(len(pl)-1):  # 구간합 구하기
    pl[i+1] += pl[i]

ans = 0
s, e = 0, 0
while 1:
    try:  # 인덱스 에러를 처리하기 위해(try~except 이용)
        if pl[e] -pl[s] < N:
            e += 1
        elif pl[e] - pl[s] > N:
            s += 1
        else:
            ans += 1
            s += 1
    except:
        break

print(ans)
