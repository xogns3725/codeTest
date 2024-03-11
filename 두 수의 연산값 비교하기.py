def solution(a, b):
    ab_sum = int(''.join((str(a),str(b))))
    return ab_sum if ab_sum>=2*a*b else 2*a*b