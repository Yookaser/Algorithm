# 1983. 조교의 성적 매기기

def grade(grade_list, students, student):
    for i, (mid, fin, hws) in enumerate(grade_list): # 인덱스값, 중간고사, 기말고사, 과제
        grade_list[i].append(mid * 0.35 + fin * 0.45 + hws * 0.2) # 비율을 반영한 새로운 점수를 각 리스트에 추가

        if i == (K - 1): # 찾고자 하는 인덱스인 경우
            K_student = grade_list[i] # 해당 값 저장

    grade_list.sort(key = lambda x: x[3], reverse = True) # 새로운 점수를 기준으로 정렬
    return grade_type[grade_list.index(K_student) // (students // 10)] # 해당 인덱스값을 찾고, grade_type를 이용하여 출력(이때, 학생 수에 따라 달라지는 것을 고려)

grade_type = {0:'A+', 1:'A0', 2:'A-', 3:'B+', 4: 'B0', 5:'B-', 6:'C+', 7:'C0', 8:'C-', 9:'D0'}
T = int(input())

for _ in range(T):
    N, K = list(map(int,input().split()))
    score_list = []
    for i in range(N):
        score_list.append(list(map(int, input().split())))
    
    print(f'#{_ + 1}', grade(score_list, N, K))