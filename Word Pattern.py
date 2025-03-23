def wordPattern(pattern, s):
    ps = {}
    sp = {}
    words = s.split()
    if (len(pattern) != len(words)):
        return False

    for i in range(len(words)):
        if pattern[i] not in ps or words[i] not in sp:
            if pattern[i] not in ps and words[i] not in sp:
                ps[pattern[i]] = words[i]
                sp[words[i]] = pattern[i]
            else:
                return False
        else:
            if ps[pattern[i]] != words[i] or sp[words[i]] != pattern[i]:
                return False
        
    return True
