def solution(n):
    answer = set()
    for i in range(n+1):
        if i != 0:
            answer.add(i if n%i==0 else 0)
    return answer

print(solution(20))