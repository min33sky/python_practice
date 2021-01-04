def correct_sentence(text: str):
    # 첫 문자를 대문자로 변환
    text = text[0].upper() + text[1:]

    # 문장이 .으로 끝나는지 확인
    if not text.endswith("."):
        text += "."

    return text


print(correct_sentence("greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends.") == "Greetings, friends.")
