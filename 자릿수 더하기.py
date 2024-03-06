def solution(n):
    # 정수값을 입력받으므로 먼저 str(n)을 사용해 문자열로 변경
    # 각 자릿수 마다 매핑을 해서 리스트에 정수화해서 저장
    # sum을 사용해 저장한 값들을 다 더해준다
    answer = sum(list(map(int, str(n))))
    return answer