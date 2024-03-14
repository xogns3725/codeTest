def solution(strArr):
    answer = []
    for sA in strArr:
        if "ad" not in sA:
            answer.append(sA)
    return answer