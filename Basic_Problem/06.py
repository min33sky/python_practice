def popular_words(text: str, word: list):
    text = text.lower().split(" ")
    result = {}
    for item in word:
        result[item] = text.count(item)
    return result


print(
    popular_words(
        "When I was One I had just begun When I was Two I was nearly new",
        ["i", "was", "three", "near"],
    )
    == {"i": 4, "was": 3, "three": 0, "near": 0}
)

