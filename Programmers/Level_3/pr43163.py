# 43163. 단어 변환

def solution(begin, target, words):
    ans = 51
    
    
    def isgo(a, b):  # 알파벳이 하나 차이나는지 검사하는 함수
        t = 0
        for i, j in zip(a, b):
            if i != j: t += 1
            if t > 1:
                return False
        return True
    
    
    def dfs(w, c, v):
        nonlocal ans
        if w == target:  # base case
            if ans > c:
                ans = c
            return
        
        for word in words:
            if w != word:  # 같은 경우는 isgo 함수가 걸러주지 않음
                if word not in v and isgo(w, word):  # 방문한 적 없고 isgo가 True를 반환하는 경우
                    v.add(word)
                    dfs(word, c+1, v)  # 백트래킹
                    v.remove(word)
        
        
    dfs(begin, 0, set())        
    
    if ans == 51:  # 갱신된 적 없는 경우
        return 0
    return ans
