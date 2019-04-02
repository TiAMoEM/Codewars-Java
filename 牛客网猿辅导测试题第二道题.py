def takePhoto(num, str):
    """
    猿辅导第二道题
    :param num: 字符串长度
    :param str: 字符串
    :return:
    """
    k = num // 3
    n = 0
    for i in range(k):
        print(" " * i + str[n] + " " * (2 * (k - i) - 1) + str[n + 1])
        n += 2
    for j in range(2 * k, num):
        print(" " * k + str[j])