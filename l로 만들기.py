def solution(myString):
    answer = ''
    for i in myString:
        if i in 'abcdefghijk':
            answer += 'l'
        else:
            answer += i
    return answer