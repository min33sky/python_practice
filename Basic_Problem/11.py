def find_message(text: str):
    return "".join(filter(str.isupper, text))


print(find_message("How are you? Eh, ok. Low orLower? Ohhh."))
print(find_message("hello world!"))
