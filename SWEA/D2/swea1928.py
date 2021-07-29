# 1928. Base64 Decoder

# 디코딩 함수
def Decoder(arr):
    Binary_list2 = '' # Base64 색인표로 변환한 값을 이진수로 바꿔서 저장할 공간
    Decoder_list = [] # 디코더된 값을 저장할 공간

    for i in arr: # 문자 -> Base64 색인표 숫자 -> 이진수로 변환 후 저장
        Binary_list2 += bin(Base64_list.index(i))[2:].rjust(6, '0') # 0b는 제거 후 rjust()로 6칸을 맞춤

    for i in range(8, len(Binary_list2)+1, 8): # 8비트(8칸)씩 읽도록(**주의** 시작이 0이되면 안됨)
        Decoder_list.append(chr(int('0b' + Binary_list2[i-8:i], base = 2)))

    return ''.join(Decoder_list)
    

# # 인코딩 함수(필요 없음)
# def Encoder(arr):
#     Binary_list1 = '' # Base64 색인표로 변환한 값을 이진수로 바꿔서 저장할 공간
#     Encoder_list = [] # 인코더된 값을 저장할 공감

#     for i in arr: # 문자 -> ASCII 숫자 -> 이진수로 변환 후 저장
#         Binary_list1 += bin(ord(i))[2:].rjust(8, '0') # 0b는 제거 후 rjust()로 8칸을 맞춤
    
#     for i in range(6, len(Binary_list1)+1, 6): # 6비트(6칸)씩 읽도록(**주의** 시작이 0이되면 안됨)
#         Encoder_list.append(Base64_list[int('0b' + Binary_list1[i-6:i], base = 2)]) # int(값, 진수) / 슬라이싱은 [i-6:i]로 해야 함

#     Solu = Decoder(Encoder_list)
#     return Solu

# Base64 색인표 생성(인덱스: 숫자, 인덱스의 값: 문자)
Base64_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

T = int(input())

for _ in range(T):
    arr = list(input())
    print(f'#{_ + 1} {Decoder(arr)}')