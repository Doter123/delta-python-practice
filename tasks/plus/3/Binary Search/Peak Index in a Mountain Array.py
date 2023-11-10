# Массив arr является горой, верните индекс пика горы (найдите пик горы)
# Вы должны решить ее по O(log(arr.length)) временной сложности.

arr = [3,9,8,6,4]

def peakIndexInMountainArray(arr: List[int]) -> int:
        
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]: return mid
            if arr[mid-1] < arr[mid]: l = mid + 1
            else: r = mid

        return 0

print(peakIndexInMountainArray(arr))