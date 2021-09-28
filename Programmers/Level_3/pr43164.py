# 43164. 여행경로

from collections import defaultdict


def solution(tickets):
    ans, dic = ["ZZZZ"], defaultdict(list)  # 최댓값으로 설정
    for ticket in tickets:  # list -> dict로 변환(tickets)
        dic[ticket[0]].append(ticket[1])  # value(list)에 추가
    
    for key in dic:  # value(list) 정렬
        dic[key].sort(reverse=True)
    

    def dfs(s, c, v):
        nonlocal ans
        if c == len(tickets):
            if ans > v:  # 더 작은 경우(알파벳 순서가 더 앞인 경우)
                ans = v[:]
            return
        
        if dic.get(s):
            for i in reversed(dic[s]):  # 뒤에서부터 탐색(for문 내부에서 리스트를 변경하므로)
                v.append(i)
                dic[s].remove(i)  # 해당 i 제거(이 부분이 느려지는 부분이라 생각)
                dfs(i, c+1, v)  # 분할 정복
                dic[s].append(i)
                v.pop()
        else:  # 해당 상황에서 다음으로 갈 공항이 없는 경우
            return
    
    dfs("ICN", 0, ["ICN"])
    return ans
