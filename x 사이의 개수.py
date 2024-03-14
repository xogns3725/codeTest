def solution(myString):
    answer = []
    str_list = myString.split('x')
    for st in str_list:
        answer.append(len(st))
    return answer