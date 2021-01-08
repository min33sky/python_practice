def home_password(text: str):
    if len(text) < 10:
        return False

    if text.upper() == text:
        return False

    if text.lower() == text:
        return False

    return any(item.isdigit() for item in text)


print(home_password("A1213pokl"))
print(home_password("bAse730onE"))
print(home_password("asasasssaaaasasaasasasasaas"))
print(home_password("QWERTYqwerty"))
print(home_password("123456123456"))
print(home_password("qwErTY1223123popqqqqq"))
