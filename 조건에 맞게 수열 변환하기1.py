def solution(arr):
    for i, a in enumerate(arr):
        # 50보다 크거나 같은 짝수
        if a>=50 and a%2==0:
            arr[i] = a//2
        # 50보다 작은 홀수
        elif a<50 and a%2==1:
            arr[i] = a*2
    return arr