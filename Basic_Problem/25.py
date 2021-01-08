def verify_anagrmas(text: str, arg: str):
    return sorted(text.lower().replace(" ", "")) == sorted(arg.lower().replace(" ", ""))


print(verify_anagrmas("Programming", "Gram Ring Mop"))
print(verify_anagrmas("Hello", "Ole Oh"))
print(verify_anagrmas("Kyoto", "Tokyo"))
