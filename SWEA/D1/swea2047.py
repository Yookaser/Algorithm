# 2047. 신문 헤드라인

# 방법1
# print(input().upper())

# 방법2
dic = {}
small_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, j in enumerate('abcdefghijklmnopqrstuvwxyz'):
    dic[j] = small_list[i]

arr = input()
for i in arr:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        print(dic[i], end = '')
    else:
        print(i, end = '')