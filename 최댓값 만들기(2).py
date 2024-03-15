def solution(numbers):
    # numbers.sort()
    # minus_max = numbers[0]*numbers[1]
    # plus_max = numbers[-1]*numbers[-2]
    # if minus_max > plus_max:
    #     return minus_max
    # return plus_max

    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])