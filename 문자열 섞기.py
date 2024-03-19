def solution(str1, str2):
    # answer = ''
    # for i in range(len(str1)):
    #     answer += str1[i] + str2[i]
    # return answer

    # join을 사용하여 리스트를 문자열로 결합
    return ''.join([str1[i] + str2[i] for i in range(len(str1))])