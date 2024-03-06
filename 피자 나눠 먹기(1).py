def solution(n):
    if n == 1:
        return 1
    # n이 1일 경우 한 번만 실행되는데
    # 이 때, i는 0이므로 if 0*7>=1이 된다
    # 따라서 위처럼 n=1일떄 1을 반환하도록 설정해야함
    for i in range(n):
        if i*7 >= n:
            return i