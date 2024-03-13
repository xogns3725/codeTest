def solution(my_string, is_suffix):
    for i in is_suffix:
        if is_suffix[-1] == my_string[-1] and len(is_suffix) <= len(my_string):
            return 1
        return 0

    # return int(my_string.endswith(is_suffix))