# 1064. 평행사변형 
import math

def Parallelogram(x1, y1, x2, y2, x3, y3):
    if (x1 - x2) * (y1 - y3) == (y1 - y2) * (x1 - x3): # 한 직선의 있는지 판별(본래 기울기 공식을 쓰면 분모가 0인 경우를 고려해야 하므로 곱으로 변환)
        return -1.0

    perimeters = [
                  math.sqrt((x1 - x2)**2 + (y1 - y2)**2),
                  math.sqrt((x1 - x3)**2 + (y1 - y3)**2),
                  math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    ] # 세 점으로 만든 세 변의 길이를 저장하는 공간
    
    return (max(perimeters) - min(perimeters)) * 2 # 평행사변형 특징(마주보는 대변이 평행하며 길이가 같음) 

A1, A2, B1, B2, C1, C2 = list(map(int, input().split()))

print(Parallelogram(A1, A2, B1, B2, C1, C2))