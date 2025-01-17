def myAtoi(s: str) -> int:
    s = s.strip()
    started = False
    neg = False
    number = 0
    if s == "":
        pass
    elif s[0] == '-':
        neg = True
        started = True
    elif s[0] == '+':
        started = True
    elif s[0].isdigit():
        number += int(s[0])
        started = True
    if started:
        for i in range(1, len(s)):
            if s[i].isdigit():
                number *= 10
                number += int(s[i])
            else:
                break
    if neg:
        number = -number
    if number > 2147483647:
        number = 2147483647
    elif number < -2147483648:
        number = -2147483648
    return number
                