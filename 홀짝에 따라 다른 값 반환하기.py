def solution(n):
    result = 0
    while n>=1:
        if n%2==1:
            result += n
            n -= 2
        else:
            result += n**2
            n -= 2
    return result