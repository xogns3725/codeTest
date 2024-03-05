def solution(str1, str2):
    answer = 0
    # str1 안에 str2가 있는지 확인
    if str2 in str1:
        answer = 1
    else: answer = 2
    return answer

