def isPalindrome(s):
    x = 0
    y = 1
    for i in range(len(s)//2):
        l = s[i + x]
        r = s[-(i + y)]
        if i + x >= len(s) - (i + y):
                return True
        while not l.isalnum():
            x += 1
            l = s[i + x]
            print(len(s))
            if i + x == len(s) - (i + y):
                return True
        while not r.isalnum():
            y += 1
            r = s[-(i + y)]
            if i + x == len(s) - (i + y):
                return True
        if l.lower() != r.lower():
            return False
    return True
