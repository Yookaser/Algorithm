# 2050. 알파벳을 숫자로 변환

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}

for i in range(len(alphabet)):
    dic[alphabet[i]] = i + 1

arr = list(input())

for i in arr:
    print(dic[i], end = ' ')