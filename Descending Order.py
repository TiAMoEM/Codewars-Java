def Descending_Order(num):
    """
    codewars练习题  Descending Order
    :param num:
    :return:
    """
    if num == 0:
        return 0
    arr = []
    s = ''
    while num > 0:
        arr.append(num % 10)
        num = num // 10
    arr.sort()
    arr.reverse()
    for i in arr:
        s += str(i)
    return int(s)