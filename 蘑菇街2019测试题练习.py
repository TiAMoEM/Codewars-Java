def move(m, n):
    """
    蘑菇街2019测试题练习
    :param m: 横轴格子数
    :param n: 纵轴格子数
    :return:
    """
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return move(m - 1, n) + move(m, n - 1)