def encode(strs):
    n = ""
    lengths = []
    for item in strs:
        lengths.append(len(item))
        for c in item:
            n += chr(ord(c) + 1)
    for length in lengths:
        n += '|' + str(length)
    n += '|'
    return n

def decode(s):
    n = ""
    d = []
    start = 0
    lengths = []
    i = 0
    while i < len(s):
        if s[i] == '|':
            g = ""
            i += 1
            while i < len(s) - 1:
                g += s[i]
                i += 1
                if s[i] == '|':
                    lengths.append(int(g))
                    break
        else:
            i += 1
    for c in s:
        if c == "|":
            break
        n += chr(ord(c) - 1)
    for i in range(len(lengths)):
        d.append(n[start:start + lengths[i]])
        start += lengths[i]
    return d
