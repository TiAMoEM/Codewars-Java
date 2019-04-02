def dig_pow(n, p):
    arr = []
    x = n
    while (n > 0):
        arr.append(n % 10)
        n = n // 10
    arr.reverse()
    k = 0
    for i in range(len(arr)):
        k += arr[i] ** (p + i)
    if k % x == 0:
        return k // x
    else:
        return -1