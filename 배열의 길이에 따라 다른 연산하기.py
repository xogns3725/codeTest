def solution(arr, n):
    answer = []
    # if len(arr)%2==1:
    #     for i in range(len(arr)):
    #         if i%2==0:
    #             answer.append(arr[i]+n)
    #         else:
    #             answer.append(arr[i])
    # else:
    #     for i in range(len(arr)):
    #         if i%2==1:
    #             answer.append(arr[i]+n)
    #         else:
    #             answer.append(arr[i])
    # return answer

    for i in range(len(arr)):
        if (len(arr) % 2 == 1 and i % 2 == 0) or len(arr) % 2 == 0 and i % 2 == 1:
            answer.append(arr[i] + n)
        else:
            answer.append(arr[i])
    return answer