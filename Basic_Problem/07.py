def bigger_price(num: int, arr: list):
    # print(sorted(arr, key=lambda x: x["price"], reverse=True)[:num])
    return sorted(arr, key=lambda x: x["price"], reverse=True)[:num]


print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meal", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
    == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
)

print(
    bigger_price(1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}])
    == [{"name": "whiteboard", "price": 170}]
)
