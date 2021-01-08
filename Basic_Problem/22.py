def monkey_typing(text: str, words: dict):
    text = text.lower()
    count = 0

    for word in words:
        if word in text:
            count += 1

    return count


print(monkey_typing("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3)
print(monkey_typing("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2)
print(
    monkey_typing(
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
        {"sum", "hamlet", "infinity", "anything"},
    )
    == 1
)

