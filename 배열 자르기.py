def solution(numbers, num1, num2):
    # 리스트 슬라이싱은 시작 인덱스는 포함하지만 종료 인덱스는 포함하지 않는다
    # 따라서 종료 인덱스에 +1을 해줘야한다
    return numbers[num1:num2+1]