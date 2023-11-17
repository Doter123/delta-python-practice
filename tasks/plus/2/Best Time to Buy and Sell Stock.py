# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1099825071/

# Вам дан массив prices, там храняться цены акции на текущий день
# Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции и выбрав другой день в будущем для продажи этой акции.

# Верните максимальную прибыль, которую вы можете получить от этой сделки. Если вы не можете получить никакой прибыли, верните '0'.


def maxProfit(prices: [int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0