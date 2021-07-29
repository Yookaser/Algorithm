# 2920. 음계

scale = list(map(int, input().split()))

if scale == sorted(scale): # 오름차순일 경우
    print('ascending')
elif scale == sorted(scale, reverse = True): # 내림차순일 경우
    print('descending')
else: # 섞인 경우
    print('mixed')