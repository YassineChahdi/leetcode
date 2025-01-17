# Third try
def trap(height):
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]
    water = 0

    while l < r:
        c = min(maxL, maxR)

        if height[l] < c:
            water += c - height[l]
        elif height[r] < c:
            water += c - height[r]

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        
        if height[l] > maxL:
            maxL = height[l]
        elif height[r] > maxR:
            maxR = height[r]
        
    return water

# Second try
def trap2(height):
    water = 0

    for i in range(1, len(height)):
        l = max(height[:i])
        r = max(height[i:])
        c = min(l, r) - height[i]
        if c > 0:
            water += c
    
    return water

# First try
def trap3(height):
    top = max(height)
    water = 0

    for h in range(top):
        l = 0
        r = len(height) - 1
        rfound = False
        lfound = False
        while l < r:
            if not lfound and height[l] > h:
                lfound = True
                
            if not rfound and height[r] > h:
                rfound = True
            
            if rfound and lfound:
                r -= 1
                l += 1
                while r >= l:
                    if height[r] <= h and r == l:
                        water += 1
                    elif height[r] <= h and height[l] <= h:
                        water += 2
                    elif height[r] <= h or height[l] <= h:
                        water += 1
                    r -= 1
                    l += 1
            
            if not rfound:
                r -= 1
            if not lfound:
                l += 1
 
    return water
