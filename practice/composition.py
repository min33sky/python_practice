# composition

squares = []

for n in range(10):
    squares.append(n ** 2)

print(squares)

new_squares = [n ** 2 for n in range(10)]

print(new_squares)

######################################################

items = "가위", "바위", "보"

results = []

for a in items:
    for b in items:
        if a != b:
            results.append((a, b))

print(results)


new_results = [(a, b) for a in items for b in items if a != b]

print(new_results)


#########################################################

a = set()

for x in "abracadabra":
    if x not in "abc":
        a.add(x)

print(a)


new_a = {x for x in "abracadabra" if x not in "abc"}

print(new_a)


#########################################################

squares = {}

for x in (2, 4, 6):
    squares[x] = x ** 2

print(squares)

new_squares = {x: x ** 2 for x in (2, 4, 6)}

print(new_squares)
