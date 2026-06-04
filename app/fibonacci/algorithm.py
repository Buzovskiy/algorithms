def fib(n):
    """
    Get Fibonacci number
    :param n: integer
    :return: integer
    """
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(7))

