def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(n):
        ways = a + b
        a = b
        b = ways
    return ways
