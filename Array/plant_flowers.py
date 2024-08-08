"""
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""
def plant_flowers(flowerbed, n):
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            prev_spot = (i == 0) or (flowerbed[i-1] == 0)
            next_spot = (i == length - 1) or (flowerbed[i+1] == 0)

            if prev_spot and next_spot:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True

    return False

print(plant_flowers([1,0,0,0,1], 1))
