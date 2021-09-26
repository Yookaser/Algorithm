# 42860. 조이스틱

def solution(name):
    dic = {}
    name = list(name)  # 값 변경을 위해 리스트로 변경
    check = len([i for i in name if i != 'A'])  # 바꿔야 하는 문자 카운팅
    for i in range(65, 91):  # 알파벳 변경을 위한 값 미리 구하기
        dic[chr(i)] = min(i - 65, 91 - i)

    ans, s = 0, 0
    for _ in range(check):
        l, r = 0, 0
        while name[s-l] == 'A':  # 왼쪽 이동
            l += 1
        while name[s+r] == 'A':  # 오른쪽 이동(둘 중 더 적은 방향으로 움직임)
            r += 1
        
        s += (-l if l < r else r)
        ans += (l if l < r else r) + dic[name[s]]  # line18~20은 순서 바뀌면 안됨
        name[s] = 'A'
        
    return ans
