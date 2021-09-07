# 43162. 네트워크

def solution(n, computers):
    ans = 0
    v = [False] * n  # 방문을 표시할 리스트
    
    def bfs(s):
        q = [s]
        
        while q:
            node = q.pop()
            
            for i in range(n):
                if computers[node][i] == 1 and not v[i]:  # 방문한 적 없고 연결되어 있는 경우(방문 표시를 앞에 놔야 시간 단축)
                    v[i] = True  # 방문 표시
                    q.append(i)  # 큐에 푸쉬
    
    for i in range(n):
        if not v[i]:  # 방문한 적 없는 경우
            bfs(i)
            ans += 1  # 카운트
            
    return ans
