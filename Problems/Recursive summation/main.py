def rec_sum(n):
    if n == 1:
        return 1
    return n + rec_sum(n - 1)
