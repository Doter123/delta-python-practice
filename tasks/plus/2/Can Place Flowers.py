flowerbed = [1,0,0,0,0,1]
n = 2

def canPlaceFlowers(flowerbed: [int], n: int) -> bool:
        
    for i in range(len(flowerbed)):
        start = i-1
        end = i+2
        if start < 0: start = 0
        if not (1 in flowerbed[slice(start, end)]):
            n -= 1
            flowerbed[i] = 1
    return n <= 0

print(canPlaceFlowers(flowerbed, n)) # False
print(canPlaceFlowers([0,0,1,0,1,0,1], 1)) # True
print(canPlaceFlowers([1,0,0,0,0,0,1], 2)) # True
print(canPlaceFlowers([1,0,0,1,0,0,1], 2)) # False
print(canPlaceFlowers([1,0,1,0,0,0,1], 2)) # False
print(canPlaceFlowers([1,0,1,0,1,0,0], 1)) # True
