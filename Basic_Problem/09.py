def checkio(*arg):
    if not arg:
        return 0
    max_val = max(arg)
    min_val = min(arg)
    return round(max_val - min_val, 1)


print(checkio(1, 2, 3))
print(checkio(5, -5))
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
print(checkio())
