def solution(myString):
    answer = [n for n in myString.split('x') if n.strip()]
    answer.sort()
    return answer