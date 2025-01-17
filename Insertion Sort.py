def insertionSort(pairs):
    if pairs == []:
        return pairs
    else:
        current = [pairs.copy()]
        for i in range(1, len(pairs)):
            for j in range(0, i):
                if pairs[i].key < pairs[j].key:
                    temp = pairs[i]
                    pairs.remove(pairs[i])
                    pairs.insert(j, temp)
                    break
            current.append(pairs.copy())
        return current
