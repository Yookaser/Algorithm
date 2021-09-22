# 3273. 두 수의 합

n = int(input())
A = set(map(int, input().split()))
x = int(input())

ans = 0
for i in A:
    if (x-i) in A:  # i < j는 고려할 필요 없음(어차피 둘 다 들어가기 때문)
        ans += 1

print(ans//2)  # 둘 다 들어왔으므로 //2
