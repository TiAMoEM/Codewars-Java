def longest_consec(strarr, k):
    """
    codewars练习题  Consecutive strings
    :param strarr:
    :param k:
    :return:
    """
    result = ''
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""
    for index in range(len(strarr) - k + 1):
        s = ''.join(strarr[index: index + k])
        if len(s) > len(result):
            result = s
    return result