def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in answer:
            answer += my_string[i]
    return answer

    # dict.fromkeys를 사용한 풀이
    # return ''.join(dict.fromkeys(my_string))