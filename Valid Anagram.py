def isAnagram(s, t):
    if sorted(s) != sorted(t):
        return False
    return True
