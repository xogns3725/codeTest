def solution(slice, n):
    if slice >= n:
        return 1
    for i in range(2, n):
        if slice*i >= n:
            return i