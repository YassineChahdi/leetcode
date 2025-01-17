def twoSum(numbers, target):
    hashmap = {} #val: index
    ans = []
    for i in range(len(numbers)):
        if target - numbers[i] in hashmap.keys():
            ans.append(hashmap[target - numbers[i]])
            ans.append(numbers.index(numbers[i], hashmap[target - numbers[i]]) + 1)
            return ans
        else:
            hashmap[numbers[i]] = i + 1

def twoSumOnePass(numbers, target):
    i = 0
    j = -1

    while True:
        if len(numbers) + j <= i:
            return "not found"
        elif numbers[i] + numbers[j] == target:
            return [i + 1, len(numbers) + j + 1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
