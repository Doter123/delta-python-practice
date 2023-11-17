# 'candies' - конфеты у детей
# 'extraCandies' - дополнительные конфеты для каждого
# Надо узнать наибольшее ли количеством конфет у детей в сравнений с тем максимумом который был до того как им всем выдали дополнительные конфеты
# Верните массив boolean значений
# К примеру: [2,3,5,1,3] - тут максимум 5
# если каждому прибавить extraCandies = 3 то у каждого будет [5,6,8,4,6]
# верните массив где вместо количество конфет у детей будет boolean значение - ( больше ли у ребёнка конфет чем изначальный максимум (который кстати был равен = 5) ? )

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    
    return list(map(lambda n: (n + extraCandies) >= max(candies), candies))

print(kidsWithCandies([2,3,5,1,3], 3)) # [True, True, True, False, True]
print(kidsWithCandies([4,2,1,1,2], 1)) # [True, False, False, False, False]
print(kidsWithCandies([12,1,12], 10)) # [True, False, True]