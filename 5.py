# prices = list()
# for index in range(20):
#    prices.append(input('Введите цену: '))
# print(prices)
prices = [23, 32.03, 94.8, 9869.5, 9.05, 10.4, 23.87, 87, 56.9, 34.7, 21, 45, 56.8, 58.70, 43.8, 45.0, 3.66, 66.7, 23.8, 45]
for price in prices:
    price = str(price)
    price_parts = price.split(".")
    # print(price_parts)
    if len(price_parts[0]) < 2:
        rubles = "0" + price_parts[0]
    else:
        rubles = price_parts[0]
    if len(price_parts) < 2:
        kopecks = "00"
    else:
        kopecks = price_parts[1]
        if len(kopecks) < 2:
            kopecks = kopecks + "0"
    print(f'{rubles} руб {kopecks} коп', end=", ")
print("")
print('ID объекта не сортированного - ', id(prices))
prices.sort()
print(prices)
print('ID объекта сортированного - ', id(prices))
prices_reversed = sorted(prices, reverse=True)
print(prices_reversed)
expensive_items = prices_reversed[:6]
print(sorted(expensive_items))
