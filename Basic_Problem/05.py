# def best_stock(stock: dict):
#     max_price = 0
#     answer = ""

#     for s in stock:
#         if stock[s] > max_price:
#             max_price = stock[s]
#             answer = s

#     return answer


def best_stock(stock: dict):
    return sorted(stock.items(), key=lambda x: x[1], reverse=True)[0][0]


print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX")
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI")

