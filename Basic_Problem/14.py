def left_join(lst: tuple):
    return ",".join(lst).replace("right", "left")


print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright alignt", "ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))

