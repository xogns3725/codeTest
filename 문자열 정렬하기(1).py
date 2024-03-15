def solution(my_string):
    answer = []
    my_str = map(str,my_string)
    for i in my_str:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer