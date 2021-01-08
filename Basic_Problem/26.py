def camel_case(text: str):
    return text.title().replace("_", "")


print(camel_case("my_function_name"))
print(camel_case("i_phone"))
print(camel_case("this_function_is_empty"))
print(camel_case("name"))
