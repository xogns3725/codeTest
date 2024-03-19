def solution(a, b):
    answer = 0
    for i in range(abs(a-b)+1):
        if b>a:
            answer += i+a
        else:
            answer += i+b
    return answer