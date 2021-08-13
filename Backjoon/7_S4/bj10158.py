# 10158. 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = w - (p+t) % w if ((p+t)//w) % 2 else (p+t) % w
y = h - (q+t) % h if ((q+t)//h) % 2 else (q+t) % h
print(x, y)