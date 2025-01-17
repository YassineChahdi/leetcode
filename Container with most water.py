def maxArea(height):
    l = 0
    r = len(height) - 1
    max = min(height[l], height[r]) * (r - l)

    while r > l:
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
        if min(height[l], height[r]) * (r - l) > max:
            max = min(height[l], height[r]) * (r - l)

    return max


def maxArea2(height):
    max = 0
    
    for i in range(len(height)):
         for j in range(i + 1, len(height)):
            new = min(height[i], height[j]) * (j - i)
            if  new > max:
                max = new

    return max
