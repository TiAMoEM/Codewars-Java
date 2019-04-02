def bus(m, n, arr):
    """
    猿辅导第一道题
    :param m:       员工数
    :param n:       大巴容量
    :param arr:     员工工号
    :return ans:    员工上车顺序
    """
    ans = []
    k = m % n
    l = m // n
    for i in range(k, 0, -1):
        ans.append(arr[i * (-1)])
    while l > 0:
        for i in range(n):
            ans.append(arr[(l - 1) * n + i])
        l -= 1
    return ans