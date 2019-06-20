def factorial(n):
    """
    codewars 练习题: Factorial
    :param n:
    :return:
    """
    if n == 0 or n == 1:
        return 1
    ans = 1
    while(n > 1):
        ans *= n
        n -= 1
    return ans