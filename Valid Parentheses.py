def isValid(s):
    stack = []
    opens = ['{', '[', '(']
    closes = ['}', ']', ')']
    for char in s:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if len(stack) == 0:
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            stack.pop(-1)
    if len(stack) != 0:
        return False
    return True
