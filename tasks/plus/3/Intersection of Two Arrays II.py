# Пересечение двух массивов II.
# Учитывая два целочисленных массива 'nums1' и 'nums2', верните массив их пересечения.
# Каждый элемент результата должен появляться столько раз, сколько он отображается в обоих массивах, и вы можете возвращать результат (в любом порядке).


from collections import Counter
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    cnt_1 = Counter(nums1)
    cnt_2 = Counter(nums2)
    for num, count in cnt_1.items():
        if num in cnt_2:
            ans += [num] * min(count, cnt_2[num])
    return ans

print(intersect([1,2,2,1], [2,2])) # [2,2]
print(intersect([4,9,5], [9,4,9,8,4])) # [4,9]
print(intersect([4,9,4,5], [9,4,9,8,4])) # [4,4,9]
