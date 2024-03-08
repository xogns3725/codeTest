def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    if sum(num_list)**2 > mul:
        return 1
    return 0