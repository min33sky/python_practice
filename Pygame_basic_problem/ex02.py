# correct sentence
# https://py.checkio.org/mission/correct-sentence/solve/


def correct_sentence(text: str) -> str:
    print(text[0].upper() + text[1:] + ("." if text[-1] != "." else ""))
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


correct_sentence("Greetings, friends.")

