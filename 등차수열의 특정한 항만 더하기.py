def solution(a, d, included):
    answer = 0
    for i in range(1, len(included)+1):
        if included[i-1]:
            answer += a + (i-1)*d
    return answer

print(solution(3, 4, [True, False, False, True, True]))