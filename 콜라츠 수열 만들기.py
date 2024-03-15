def solution(n):
    # 연산횟수 0인 경우 n값 그대로 반환하므로 시작요소에 n추가
    answer = [n]
    while n!=1:
        if n%2==0:
            n //= 2
            answer.append(n)
        else:
            n = (3*n) + 1
            answer.append(n)
    return answer