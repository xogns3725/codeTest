def solution(x):
    if x % sum(map(int, str(x))) == 0:
        return True
    return False

    # return True if x % sum(map(int, str(x))) == 0 else False