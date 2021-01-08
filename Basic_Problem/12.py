def three_words(text: str):
    text = text.split(" ")
    count = 0
    for s in text:
        if s.isalpha():
            count += 1
        else:
            count = 0

        if count >= 3:
            return True

    return False


print(three_words("Hello World hello"))
print(three_words("He is 123 man"))
print(three_words("1 2 3 4"))
print(three_words("bla bla bla bla"))
print(three_words("Hi"))
