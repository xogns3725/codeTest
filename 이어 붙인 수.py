def solution(num_list):
    # 홀수, 짝수 배열 생성
    odd = []
    even = []
    # 각각의 배열에 값 집어넣기
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(str(num_list[i]))
        else:
            odd.append(str(num_list[i]))
    # join을 사용하여 하나의 문자열로 합친다
    odd_sum = ''.join(odd)
    even_sum = ''.join(even)

    return int(odd_sum) + int(even_sum)