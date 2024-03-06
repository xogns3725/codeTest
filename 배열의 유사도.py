def solution(s1, s2):
    answer = 0
    # s1과 s2 중 더 짧은 배열 선택
    min_s = min(len(s1), len(s2))
    # 더 짧은 배열을 선택해야지 인덱스 범위를 초과하지 않음
    for i in range(min_s):
        # s1이 더 긴 경우
        if len(s1) >= len(s2):
            # s1 안에 s2[i]에 해당하는 값이 있는지 확인
            if s2[i] in s1:
                answer += 1
        # s2가 더 긴 경우
        else:
            # s2 안에 s1[i]에 해당하는 값이 있는지 확인
            if s1[i] in s2:
                answer += 1
    return answer