def topKFrequent(nums, k):
    hashmap = {} # digit: count
    diffs = set(nums)
    for num in diffs:
        hashmap[num] = nums.count(num)
    hashmap = dict(sorted(hashmap.items(), key=lambda x:x[1], reverse=True))
    return list(hashmap.keys())[:k]
