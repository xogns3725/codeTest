def solution(x, n):
    answer = []
    if x == 0:
        return [0] * n
    for i in range(x, x * n + 1 if x >= 0 else x * n - 1, x):
        answer.append(i)
    return answer

    # 좀 더 간단한 방식
    # answer = []
    # for i in range(1,n+1):
    #     answer.append(x*i)
    # return answer

    # 간단한 방식 + 리스트 컴프리헨션
    # return [x*i for i in range(1,n+1)]