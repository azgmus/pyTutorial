def decimal_to_base(num, base):
    base_num = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            base_num += str(dig)
        num //= base
    base_num = base_num[::-1]
    return base_num


def sort_digits_descending(n):
    res = ''.join(sorted(list(n), reverse=True))
    return res


def sort_digits_ascending(n):
    res = ''.join(sorted(list(n), reverse=False))
    return res


def solution(n, b):
    num_of_digits = len(n)
    cur_id = n
    history = []

    while True:
        x = sort_digits_descending(cur_id)
        y = sort_digits_ascending(cur_id)
        history.append(cur_id)
        if history.count(cur_id) > 1:
            return (len(history) - 1) - history.index(cur_id)
        cur_id = decimal_to_base(int(x, base=b) - int(y, base=b), b)
        while len(cur_id) < num_of_digits:
            cur_id = '0' + cur_id






print(solution('210022', 3))
