def solution(arr):
    # answer=[]
    # for i in arr:
    #     for _ in range(i):
    #         answer.append(i)
    # return answer

    return [i for i in arr for _ in range(i)]