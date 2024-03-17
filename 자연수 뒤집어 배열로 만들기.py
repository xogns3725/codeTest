# def solution(n):
#     reversed_str = str(n)[::-1]
#     answer = [int(i) for i in reversed_str]
#     return answer

def solution(n):
    return sorted(map(int, str(n)), reverse=True)