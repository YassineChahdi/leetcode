def groupAnagrams(strs):
    hashmap = {} # sorted(word) : [anagrams...]
    for word in strs:
        if "".join(sorted(word)) in hashmap.keys():
            hashmap["".join(sorted(word))].append(word)
        else:
            hashmap["".join(sorted(word))] = [word]
    return list(hashmap.values())
