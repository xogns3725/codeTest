def solution(hp):
    answer = hp//5
    hp %= 5
    answer += hp//3
    hp %= 3
    answer += hp
    return answer