def solution(n):
    answer = 0
    while True:
        answer += 1
        if answer**2 == n:
            return (answer+1)**2
        elif answer**2 > n:
            return -1