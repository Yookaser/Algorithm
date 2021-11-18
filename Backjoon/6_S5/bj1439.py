# 1439. 뒤집기

S = input()
change = []

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        change.append(i)

isodd = 1 if len(change) % 2 == 1 else 0
result = len(change) // 2

print(result+1 if isodd else result)
