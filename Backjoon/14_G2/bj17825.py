# 17825. 주사위 윷놀이



A = list(map(int, input().split()))
G = [0] + [2 * i for i in range(1, 21)] + [13, 16, 19, 25, 30, 35] + [22, 24] + [28, 27, 26]
H = [4] + [0] * (len(G)-1)

print(G)
print(H)