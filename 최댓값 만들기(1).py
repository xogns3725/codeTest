def solution(numbers):
    max_num = max(numbers)
    numbers.remove(max_num)  # 최댓값을 제거하여 중복된 최댓값을 방지
    sec_max = max(numbers)

    return max_num * sec_max