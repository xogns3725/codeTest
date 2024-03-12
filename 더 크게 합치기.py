def solution(a, b):
    ab_sum = int(''.join((str(a),str(b))))
    ba_sum = int(''.join((str(b),str(a))))
    if ab_sum >= ba_sum:
        return ab_sum
    return ba_sum