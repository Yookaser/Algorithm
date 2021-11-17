# 2822. 점수 계산

A = [int(input()) for _ in range(8)]
B = sorted(A, reverse=True)
C = []

for i in B[:5]:
    C.append(A.index(i)+1)

print(sum(B[:5]))
print(*sorted(C))
