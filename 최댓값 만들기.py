# 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록
# solution 함수를 완성해주세요.

# O(n log n) 풀이
def solution(numbers):
    answer = 0
    sorted_numbers = sorted(numbers, reverse=True)
    answer = sorted_numbers[0]*sorted_numbers[1]
    return answer
# 시간복잡도 설명
# sorted()는 내부적으로 timesort 알고리즘 사용
# timesort 알고리즘 내부
# for i in range(...)
# ...
# while size < n:
#   ...
#   size *= 2
# 내부에서 for문 1번과 i*2씩 증가하는 반복문 사용 하므로
# O(n log n)


# O(n) 풀이
# max함수 시간복잡도 사용되고
# 모든 배열의 원소를 한번 씩 스캔, O(n)
# max함수가 max_num, sec_max 두번 호출해서 O(n)+O(n)=O(2n)
# 빅오표기법에서 상수는 무시하므로 O(2n) -> O(n)
def solution2(numbers):
    if len(numbers) < 2:
        return 0
    max_num = max(numbers)
    numbers.remove(max_num)  # 최댓값을 제거하여 중복된 최댓값을 방지
    sec_max = max(numbers)

    return max_num * sec_max

# print(solution([1,2,3,4,5]))
# print(solution([0,31,24,10,1,9]))
# print(solution([1,2]))
#
# print(solution2([1,2,3,4,5]))
# print(solution2([0,31,24,10,1,9]))
# print(solution2([1,2]))
