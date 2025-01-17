def isPalindrome(x):
    x = str(x)
    rev = x[::-1]
    if x == rev:
        return True
    return False
