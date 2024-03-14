def solution(array):
    # max_arr = 0
    # max_idx = 0
    # for i in range(len(array)):
    #     if array[i] > max_arr:
    #         max_arr = array[i]
    #         max_idx = i
    # return [max_arr, max_idx]

    return [max(array), array.index(max(array))]