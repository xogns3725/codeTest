def solution(n):
    answer = []
    # 1부터 제곱근까지 순회반복
    # 제곱근보다 큰 숫자는 약수가 될 수 없기 때문
    for i in range(1,int(n**0.5)+1):
        # i가 n의 약수일 경우
        if n%i == 0:
            answer.append((i, n//i))
            # ex) 2의 약수 출력할 경우 (1,2)만 출력되기에
            # 다음과 같은 조건을 줘서 (2,1)도 출력되게 만듬
            # 간단히 for문의 조건식을 n**2로 수정해도 실행은 되는데
            # 타임아웃 발생
            if i != n//i:
                answer.append((n//i, i))
    return len(answer)