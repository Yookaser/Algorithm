# 11719. 그대로 출력하기2

while True:
    try:
        print(input())
    except EOFError:  # 파일의 끝에 도달한 경우
        break
