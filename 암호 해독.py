def solution(cipher, code):
    answer = ''
    # idx는 0부터 시작하므로 code-1
    for i in range(code-1,len(cipher),code):
        answer += cipher[i]
    return answer