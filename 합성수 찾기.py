def solution(n):
    lst = []
    for i in range(4, n + 1):
        answer = 1
        count = 0
        while answer != i + 1:
            if i % answer == 0:
                count += 1
            answer += 1
        if count >= 3:
            lst.append(i)

    return len(lst)