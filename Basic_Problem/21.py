def non_unique_elements(lst: list):
    return [item for item in lst if lst.count(item) > 1]


print(non_unique_elements([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
print(non_unique_elements([1, 2, 3, 4, 5]) == [])
print(non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
print(non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])

